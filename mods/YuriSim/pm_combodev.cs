using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Reflection;
using System.Timers;
using UnityEngine;
using PoseMod; //include pmcoreXX.dll and pmcutscenesXX.dll

// Needs to start from a namespace called "PoseMod"
namespace PoseMod
{
	// Needs to start from a class called "Module"
	public static class Module
	{
		// Function that will be executed to init the dll
		public static void Init()
		{
			"DEV plugin initiated".DebugLog();

			// Example: Adding just some scripts that do things
			// Adds your plugin as a monobehaviour into the posemod object; this object is not destroyed on scene load
			PoseMod.Core.Pm_Gameobject.AddComponent<DevPlugin>();

			// Example: Adding a new menu
			GameObject _menuRoot = new GameObject("ExampleMenu");
			_menuRoot.transform.SetParent(PoseMod.UI.UIRoot.transform);
			DevMenu _exampleMenu = _menuRoot.AddComponent<DevMenu>();
			_exampleMenu.Root = _menuRoot;

			PoseMod.UI.AddNewRootMenu(_exampleMenu);
		}
	}


	// Any class that starts with "PoseModCommands_" will be read for commands
	public class PoseModCommands_DevCommands : MonoBehaviour
	{
		public CutsceneModule ThisCutscene;
		public PoseModCommands_Core CoreCmds;

		// -----------
		// In here command function names must be written in lower case

		public void devcommand2(GameObject obj)
		{
			obj.transform.position = new Vector3(5,5,5);
		}
		public void yantodoki(GameObject obj, int i)
		{
            var x = GameObject.FindObjectOfType<DokiScript>().GetComponent<DokiScript>();
			x.Yandere.PantyAttacher.newRenderer.enabled = false;
            UnityEngine.Object.Instantiate<GameObject>(x.TransformEffect, x.Yandere.Hips.position, Quaternion.identity);
            x.Yandere.MyRenderer.sharedMesh = x.Yandere.Uniforms[4];
            x.Yandere.MyRenderer.materials[0].mainTexture = x.DokiTexture;
            x.Yandere.MyRenderer.materials[1].mainTexture = x.DokiTexture;
            if (i == 1)
            {
                x.Yandere.MyRenderer.materials[0].SetTexture("_OverlayTex", x.DokiSocks[0]);
                x.Yandere.MyRenderer.materials[1].SetTexture("_OverlayTex", x.DokiSocks[0]);
            }
            else
            {
                x.Yandere.MyRenderer.materials[0].SetTexture("_OverlayTex", x.DokiSocks[1]);
                x.Yandere.MyRenderer.materials[1].SetTexture("_OverlayTex", x.DokiSocks[1]);
            }
            Debug.Log("Activating shadows on Yandere-chan.");
            x.Yandere.MyRenderer.materials[0].SetFloat("_BlendAmount", 1f);
            x.Yandere.MyRenderer.materials[1].SetFloat("_BlendAmount", 1f);
            x.Yandere.MyRenderer.materials[2].mainTexture = x.DokiHair[i];
            x.Yandere.Hairstyle = 136 + i;
            x.Yandere.UpdateHair();

            x.Yandere.UniformTextures[StudentGlobals.FemaleUniform] = x.DokiTexture;
            x.Yandere.CasualTextures[StudentGlobals.FemaleUniform] = x.DokiTexture;
            x.Yandere.EightiesUniform = x.DokiTexture;
            x.Yandere.EightiesCasual = x.DokiTexture;
            x.Yandere.Uniforms[StudentGlobals.FemaleUniform] = x.Yandere.MyRenderer.sharedMesh;
            return;
		}

        public void studtodokiuniform(StudentScript stud){
            var x = GameObject.FindObjectOfType<DokiScript>().GetComponent<DokiScript>();
            var shoe = stud.ShoeRemoval;
			shoe.OutdoorShoes = x.DokiTexture;
			shoe.IndoorShoes = x.DokiTexture;
			stud.Cosmetic.CasualTexture = x.DokiTexture;
			stud.Cosmetic.UniformTexture = x.DokiTexture;
            shoe.TargetShoes = x.DokiTexture;
			shoe.Socks = x.DokiTexture;
            stud.MyRenderer.sharedMesh = x.Yandere.Uniforms[4];
            stud.MyRenderer.materials[0].mainTexture = x.DokiTexture;
            stud.MyRenderer.materials[1].mainTexture = x.DokiTexture;
        }

        public void allstuddokiuniform()
        {
            foreach (var stud in GameObject.FindObjectsOfType<StudentScript>())
            {
                //Could be better code but whatever
                StudentJson studentJson = stud.JSON.Students[stud.StudentID];
                if(studentJson.Gender == 0)
                {
                    studtodokiuniform(stud);    
                }
            }
        }
	}

	// Any class that starts with "PoseModConditions_" will be read for conditions
	public class PoseModConditions_DevCommands : MonoBehaviour
	{
		public CutsceneModule ThisCutscene;
		public PoseModCommands_Core CoreCmds;

		// -----------
		// In here condition function names must be written in lower case
		// Every function must return bool type

		public bool Devcondition()
		{
			// return CheckSomething();

			return false;
		}

	}

    // // remove this id you're not using it
    // // rename it if you use it
	// public class DevPlugin : MonoBehaviour
	// {
	// 	public void Start()
	// 	{

	// 	}
	// 	public void Update()
	// 	{

	// 	}
	// }


    // remove this id you're not using it
    // rename it if you use it
	public class DevMenu : PmUI_RootMenu
	{
		public DevMenu()
		{
			// Key to open and close your menu
			OpeningKey = KeyCode.F5;
		}

		public override void Init ()
		{
			base.Init ();
			// Code that executes when the menu is created

		}
		public override void Open ()
		{
			base.Open ();
			// Code that executes when the menu is opened

		}
		public override void Close ()
		{
			base.Close ();
			// Code that executes when the menu is closed

		}

		public void Start()
		{

		}
		public void Update()
		{

		}
	}
}

