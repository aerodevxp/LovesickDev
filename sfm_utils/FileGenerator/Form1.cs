using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Text.RegularExpressions;

namespace FileGenerator
{
    public partial class Form1 : Form
    {
        string path = "";
        public Form1()
        {
            InitializeComponent();
        }

        private void Label1_Click(object sender, EventArgs e)
        {

        }

        private void CheckBox1_CheckedChanged(object sender, EventArgs e)
        {
            
        }

        private void TextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Label2_Click(object sender, EventArgs e)
        {

        }


        private void RadioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
            {
                richTextBox1.Text = "Enter the number of files you want here.";
            }
        }

        private void RadioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked)
            {
                richTextBox1.Text = "Please separate each file name with a ; (semi-colon).\n Do not include the extension either.";
            }
        }

        private void Button1_Click_1(object sender, EventArgs e)
        {
            if (path == "")
            {
                string message = "Please specify a path!";
                string caption = "Uh...";
                MessageBoxButtons buttons = MessageBoxButtons.OK;
                DialogResult result;

                // Displays the MessageBox.
                result = MessageBox.Show(message, caption, buttons);
            }
            else
            {
                CreateFiles();
            }
        }

        private string SetVariables(string contentToCheck, string fileName, string fileExtension)
        {
            contentToCheck = contentToCheck.Replace("[filePath]", path);

            contentToCheck = contentToCheck.Replace("[fileName]", fileName);

            contentToCheck = contentToCheck.Replace("[fileExtension]", fileExtension);

            return contentToCheck;
        }

        public void CreateFiles()
        {
            Console.WriteLine("File Creation Started.");
            string fileExtension = GetFileExtension();

            int quantity = 0;

            if (radioButton1.Checked)
            {
                try
                {
                    quantity = Int32.Parse(richTextBox1.Text);
                }
                catch
                {
                    string message = "Please specify a number in the textbox. If you want to name your files. Use the Custom Names mode.";
                    string caption = "Uh...";
                    MessageBoxButtons buttons = MessageBoxButtons.OK;
                    DialogResult result;

                    // Displays the MessageBox.
                    result = MessageBox.Show(message, caption, buttons);
                    return;
                }
                for (int x = 0; x < quantity; x++)
                {
                    if (checkBox1.Checked)
                    {
                        FileStream fs = File.Create(path + (x + 1).ToString() + fileExtension);
                        fs.Close();
                        string txt = SetVariables(richTextBox2.Text, (x + 1).ToString(), fileExtension);
                        File.WriteAllText(fs.Name, txt);
                    }
                    else
                    {
                        if(!File.Exists(path + (x + 1).ToString() + fileExtension))
                        {
                            FileStream fs = File.Create(path + (x + 1).ToString() + fileExtension);
                            fs.Close();
                            string txt = SetVariables(richTextBox2.Text, (x + 1).ToString(), fileExtension);
                            File.WriteAllText(fs.Name, txt);
                        }
                    }
                    

                }
            }
            else if (radioButton2.Checked)
            {
                string stringofFiles = richTextBox1.Text;
                char[] delimiterChar = { ';' };
                string[] namesOfFiles = stringofFiles.Split(delimiterChar);
                foreach (var name in namesOfFiles)
                {
                    string finalName = name;
                    finalName = Regex.Replace(name, @"\t|\n|\r", "");
                    if (finalName != "" || finalName != " "){
                        if (checkBox1.Checked)
                        {
                            FileStream fs = File.Create(path + finalName + fileExtension);
                            fs.Close();
                            string txt = SetVariables(richTextBox2.Text, finalName, fileExtension);
                            File.WriteAllText(fs.Name, txt);
                        }
                        else
                        {
                            if (!File.Exists(path + finalName + fileExtension))
                            {
                                FileStream  fs = File.Create(path + finalName + fileExtension);
                                fs.Close();
                                string txt = SetVariables(richTextBox2.Text, finalName, fileExtension);
                                File.WriteAllText(fs.Name, txt);
                            }
                        }
                    }
                }
                File.Delete(path + fileExtension);
            }
        }


        public string GetFileExtension()
        {
            
            TextBox TextBox = this.textBox1;
            string TextBoxTxt = TextBox.Text;
            if (!TextBoxTxt.StartsWith("."))
            {
                TextBoxTxt = TextBoxTxt.Insert(0, ".");
            }
            Console.WriteLine("Extension is " + TextBoxTxt);
            return TextBoxTxt;
        }

        private void RichTextBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void Label3_Click(object sender, EventArgs e)
        {

        }

        private void Label4_Click(object sender, EventArgs e)
        {

        }

        private void Button2_Click(object sender, EventArgs e)
        {
            FolderBrowserDialog folderBrowserDialog1 = new FolderBrowserDialog();
            folderBrowserDialog1.ShowDialog();
            path = folderBrowserDialog1.SelectedPath + "\\";
            textBox2.Text = path;
        }

        private void RichTextBox2_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
