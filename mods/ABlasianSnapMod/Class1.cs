using MelonLoader;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using UnityEngine;
using SecondDinner;
using TMPro;
using CubeUnity.App.State;
using CubeUnity.Infra.Dev;
using CubeUnity.App;
using DarkTonic;
using DarkTonic.MasterAudio;
using System.Collections;
using UnityEngine.Networking;
using System.IO;
using Il2CppSystem.Security.Cryptography;
using System.Security.Policy;
using static Il2CppSystem.Array;
using CubeUnity.App.Admin.DevConsole;
using CubeUnity.App.Scene;
using CubeUnity;
using CubeUnity.Infra.Event;

namespace ABlasianSnapPrj
{
    public class ABlasianSnapMod : MelonMod
    {

        private float nextActionTime = 0.0f;
        public float period = 5.0f;

        private AdminManager adminManager;
        private ShopManager shopManager;
        private GameManager gameManager;
        private DevManager devManager;

        PlaylistController playlistController;

        public override void OnSceneWasLoaded(int buildIndex, string sceneName)
        {
            LoggerInstance.Msg("HI!");
            playlistController = GameObject.Find("PlaylistController(Clone)").GetComponent<PlaylistController>();

        }


        public override void OnUpdate()
        {

            if (Time.time > nextActionTime)
            {
                nextActionTime += period;
                // execute block of code here
                LoggerInstance.Msg("Update every 5 SEC!");
                LoggerInstance.Msg("=============");

                //Find AdminManager
                if(this.adminManager == null)
                {
                    LoggerInstance.Msg("O -> Fetching the AdminManager.");
                    GameObject adminHelperObj = GameObject.Find("AdminManager-Helper");
                    if(adminHelperObj != null)
                    {
                        var admin = adminHelperObj.GetComponent<CubeUnity.Infra.RuntimeScriptableObject.RuntimeScriptableObjectHelper>()._object.Cast<AdminManager>();
                        if (admin != null)
                        {
                            admin.IsGodAccount = false;
                            admin.DevConsoleEnabled = false;
                            admin.DevOptions.ShowDebugText = false;

                            this.adminManager = admin;
                            LoggerInstance.Msg("O -> AdminManager found.");
                        }
                        else
                        {
                            LoggerInstance.Msg("X -> admin is null.");
                        }

                    }
                    else
                    {
                        LoggerInstance.Msg("X -> adminHelperObj is null.");
                    }
                }

               //Find ShopManager
                if(this.shopManager == null)
                {
                    LoggerInstance.Msg("O -> Fetching the ShopManager.");
                    GameObject shopHelperObj = GameObject.Find("ShopManager-Helper");
                    if(shopHelperObj != null)
                    {
                        var manager = shopHelperObj.GetComponent<CubeUnity.Infra.RuntimeScriptableObject.RuntimeScriptableObjectHelper>()._object.Cast<ShopManager>();
                        if (manager != null)
                        {
                            

                            this.shopManager = manager;
                            LoggerInstance.Msg("O -> ShopManager found.");
                        }
                        else
                        {
                            LoggerInstance.Msg("X -> manager for Shop is null.");
                        }

                    }
                    else
                    {
                        LoggerInstance.Msg("X -> shopHelperObj is null.");
                    }
                }               
                
                //Find GameManager
                if(this.gameManager == null)
                {
                    LoggerInstance.Msg("O -> Fetching the GameManager.");
                    GameObject gameHelperObj = GameObject.Find("GameManager-Helper");
                    if(gameHelperObj != null)
                    {
                        var manager = gameHelperObj.GetComponent<CubeUnity.Infra.RuntimeScriptableObject.RuntimeScriptableObjectHelper>()._object.Cast<GameManager>();
                        if (manager != null)
                        {
                            

                            this.gameManager = manager;
                            LoggerInstance.Msg("O -> GameManager found.");
                        }
                        else
                        {
                            LoggerInstance.Msg("X -> manager for Game is null.");
                        }

                    }
                    else
                    {
                        LoggerInstance.Msg("X -> gameHelperObj is null.");
                    }
                }

                //Find DevManager
                if (this.devManager == null)
                {
                    LoggerInstance.Msg("O -> Fetching the DevManager.");
                    GameObject devHelperObj = GameObject.Find("DevManager-Helper");
                    if (devHelperObj != null)
                    {
                        var manager = devHelperObj.GetComponent<CubeUnity.Infra.RuntimeScriptableObject.RuntimeScriptableObjectHelper>()._object.Cast<DevManager>();
                        if (manager != null)
                        {
                            this.devManager = manager;
                            LoggerInstance.Msg("O -> DevManager found.");
                        }
                        else
                        {
                            LoggerInstance.Msg("X -> manager for Dev is null.");
                        }

                    }
                    else
                    {
                        LoggerInstance.Msg("X -> devHelperObj is null.");
                    }
                }



                LoggerInstance.Msg("============= UPDATE 5 SEC DONE");
            }

            if(Input.GetKeyDown(KeyCode.BackQuote))
            {
                LoggerInstance.Msg("Backquote Pressed.");
                this.DevMode();
            }
            
            if(Input.GetKeyDown(KeyCode.M))
            {
                LoggerInstance.Msg("Music Time.");
                Music();
            }
            
        }

        private void DevMode()
        {
            AudioSource audio = playlistController.gameObject.AddComponent<AudioSource>();
            audio.PlayOneShot(ReadAudio(Application.streamingAssetsPath + "/blasianfolder/sounds/devmode.wav", "devmode"));
            try
            {
                GameObject.Find("Text_Play").GetComponent<TextMeshProUGUI>().SetText("DEV!");
                FindObjectFromParent(GameObject.Find("Navigator"), "GameInfo").SetActive(true);
                FindObjectFromParent(GameObject.Find("Graphy_FPS"), "FPS - Module").SetActive(true);
                FindObjectFromParent(GameObject.Find("Graphy_FPS"), "RAM - Module").SetActive(true);
                FindObjectFromParent(GameObject.Find("Graphy_FPS"), "AUDIO - Module").SetActive(true);

            }
            catch
            {

            }
            
            devManager.ToggleConsoleKey = UnityEngine.InputSystem.Key.C;

            //List all commands from the devPages in devManager
            LoggerInstance.Msg("====== DEV PAGES LIST ======");
            for(var y = 0; y < devManager.Pages.Count; y++)
            {
                LoggerInstance.Msg(devManager.Pages[y].name + " || CARD " + devManager.Pages[y].ShowCardInput.ToString() + " || LOCATION " + devManager.Pages[0].ShowLocationInput.ToString());

                try
                {

                    int commandCount = devManager.Pages[y].TryCast<DevCommandPage>().Commands.Count;

                    for(var x = 0; x < commandCount; x++)
                    {
                        try
                        {
                            var cmd = devManager.Pages[y].TryCast<DevCommandPage>().Commands.System_Collections_Generic_IList_T__get_Item(x);
                            LoggerInstance.Msg(cmd.name + "(" + cmd.GetType().ToString() + ")");
                            if(cmd.name == "GrantAllCatalogCards" || cmd.name == "GrantAllCatalogVariants")
                            {
                                cmd.Execute();
                                LoggerInstance.Msg("Executed!");
                            }

                        }
                        catch (Exception e)
                        {
                            LoggerInstance.Msg(e);
                        }

                    }
                }
                catch (Exception e)
                {

                    LoggerInstance.Msg(e);
                }

                LoggerInstance.Msg("-----");
            }
            LoggerInstance.Msg("============================");





        }

        public static GameObject FindObjectFromParent(GameObject parent, string name)
        {
            Transform[] trs = parent.GetComponentsInChildren<Transform>(true);
            foreach (Transform t in trs)
            {
                if (t.name == name)
                {
                    return t.gameObject;
                }
            }
            return null;
        }

        private void Music()
        {

            //Need a PlaylistController
            
            MasterAudio.StopAllPlaylists();
            AudioSource audio = playlistController.gameObject.AddComponent<AudioSource>();
            audio.PlayOneShot(ReadAudio(Application.streamingAssetsPath + "/blasianfolder/sounds/music1.wav", "music1"));
        }

        private AudioClip ReadAudio(string path, string clipname)
        {
            byte[] receivedBytes = File.ReadAllBytes(path);

            WWUtils.Audio.WAV wav = new WWUtils.Audio.WAV(receivedBytes);

            AudioClip clip = AudioClip.Create(clipname, wav.SampleCount, 1, wav.Frequency, false, false);
            clip.SetData(wav.LeftChannel, 0);
            return clip;
        }

    }

}


namespace WWUtils.Audio
{
    public class WAV
    {

        // convert two bytes to one float in the range -1 to 1
        static float bytesToFloat(byte firstByte, byte secondByte)
        {
            // convert two bytes to one short (little endian)
            short s = (short)((secondByte << 8) | firstByte);
            // convert to range from -1 to (just below) 1
            return s / 32768.0F;
        }

        static int bytesToInt(byte[] bytes, int offset = 0)
        {
            int value = 0;
            for (int i = 0; i < 4; i++)
            {
                value |= ((int)bytes[offset + i]) << (i * 8);
            }
            return value;
        }

        private static byte[] GetBytes(string filename)
        {
            return File.ReadAllBytes(filename);
        }
        // properties
        public float[] LeftChannel { get; internal set; }
        public float[] RightChannel { get; internal set; }
        public int ChannelCount { get; internal set; }
        public int SampleCount { get; internal set; }
        public int Frequency { get; internal set; }

        // Returns left and right double arrays. 'right' will be null if sound is mono.
        public WAV(string filename) :
            this(GetBytes(filename))
        { }

        public WAV(byte[] wav)
        {

            // Determine if mono or stereo
            ChannelCount = wav[22];     // Forget byte 23 as 99.999% of WAVs are 1 or 2 channels

            // Get the frequency
            Frequency = bytesToInt(wav, 24);

            // Get past all the other sub chunks to get to the data subchunk:
            int pos = 12;   // First Subchunk ID from 12 to 16

            // Keep iterating until we find the data chunk (i.e. 64 61 74 61 ...... (i.e. 100 97 116 97 in decimal))
            while (!(wav[pos] == 100 && wav[pos + 1] == 97 && wav[pos + 2] == 116 && wav[pos + 3] == 97))
            {
                pos += 4;
                int chunkSize = wav[pos] + wav[pos + 1] * 256 + wav[pos + 2] * 65536 + wav[pos + 3] * 16777216;
                pos += 4 + chunkSize;
            }
            pos += 8;

            // Pos is now positioned to start of actual sound data.
            SampleCount = (wav.Length - pos) / 2;     // 2 bytes per sample (16 bit sound mono)
            if (ChannelCount == 2) SampleCount /= 2;        // 4 bytes per sample (16 bit stereo)

            // Allocate memory (right will be null if only mono sound)
            LeftChannel = new float[SampleCount];
            if (ChannelCount == 2) RightChannel = new float[SampleCount];
            else RightChannel = null;

            // Write to double array/s:
            int i = 0;
            while (pos < wav.Length)
            {
                LeftChannel[i] = bytesToFloat(wav[pos], wav[pos + 1]);
                pos += 2;
                if (ChannelCount == 2)
                {
                    RightChannel[i] = bytesToFloat(wav[pos], wav[pos + 1]);
                    pos += 2;
                }
                i++;
            }
        }

        public override string ToString()
        {
            return string.Format("[WAV: LeftChannel={0}, RightChannel={1}, ChannelCount={2}, SampleCount={3}, Frequency={4}]", LeftChannel, RightChannel, ChannelCount, SampleCount, Frequency);
        }
    }

}