
![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/logo.png?raw=true)

# NVIDIA OMNIVERSE
# How to Build Custom 3D Scene Manipulator Tools on NVIDIA Omniverse

See how you can build advanced tools on the modular, easily extensible Omniverse platform. You’ll learn from the Omniverse developer ecosystem team how you can extend and enhance the 3D tools you know and love today.​

# Learning Objectives
- Enable Extension
- Attach `scale` function to Slider Widget

<video width="560" height="315" controls>
<source src="https://d36m44n9vdbmda.cloudfront.net/assets/x-ov-06-v1/sceneManipulatorIntro.mp4" type="video/mp4">
</video>
 
# UI Scene_Widget Info

## Section I

<video width="560" height="315" controls>
<source src="https://d36m44n9vdbmda.cloudfront.net/assets/x-ov-06-v1/sceneManipulator1.mp4" type="video/mp4">
</video>
 
### Step 1: Open the Workshop Stage

#### <b>Step 1.1: Download the Stage from the Link Provided</b>

[Stage Link](https://dli-lms.s3.amazonaws.com/assets/x-ov-05-v1/Stage.zip)

#### <b> Step 1.2: Unzip Stage Using Extract All...

This creates an unzipped file folder called `Stage`.

#### <b> Step 1.3: Open Stage in Omniverse

Navigate inside Omniverse Code's `Content tab` to the stage file's location on your system.
  
(i.e. C:/Users/yourName/Downloads/Stage)
 
**Double Click** `Siggraph2022_Stage.usd` in the center window pane of the `Content tab` at the bottom of the Omniverse Code Console and it will appear in the viewport.

### Step 2: Install the Widget Extension
#### <b>Step 2.1: Open the Extensions Tab</b>

Click on `Extensions` Manager Tab 

#### <b>Step 2.2: Filter by Commnuity Extension</b>

Select `Community` tab
<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/extensionCommunity.PNG?raw=true)

<br>

#### <b>Step 2.3: Search for Widget Info</b>

Search for `Widget Info` and click on `Omni UI Scene Object Info With Widget Example`

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/widgetExt.png?raw=true)

#### <b>Step 2.4: Install/Enable the Extension</b>

Click on the extension and then click `Install` in the right console. Once installed, enable the extension. 

><span>&#10071;</span> You may get a warning that this extension is not verified. It is safe to install this extension.

<br>

#### <b>Step 2.5: Check that the Widget is Working</b>

Navigate to `Viewport` then select a `prim` in the hierarchy. 

A `prim` is short for primitive. The prim is the fundamental unit in Omniverse. Anything imported or created in a `USD`, Universal Scene Description, scene. This includes camera, sounds, lights, meshes, etc. 

You should see the following widget appear in the viewport above the `prim`:

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/viewportWidgetEnabled.PNG?raw=true)

<br>

><span>&#10067;</span> Did you notice?
>- The path of the prim is displayed in the widget.
>- There is a scale slider in the widget but it doesn't work! We will fix this in the next section.

<br>

#### <b>Step 3: Find the Play Button</b>

Locate the `Play` button in the viewport and see what happens when you click it! Don't forget to hit the `Stop` button when you are finished.

<details>
<summary>Click here to see where the button is located </summary>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/playButton.png?raw=true)

</details>

<br>

>#### <span>&#129504;</span><b>Challenge Step 4: Brainstorm Use Cases</b>
><i>All Challenges in this workshop are optional</i>
>
>Think of 3 ways a widget could be used. For example, you noticed that the path of the prim is displayed, what else could you display about the prim in the widget? Brain storm with your peers and think of how it can be used for your industry! We will have a group discussion about this later on.

<br>

<br>

>### <span>&#9940;</span> Stop here and wait to move on to Section II

<br>

## Section II

<video width="560" height="315" controls>
<source src="https://d36m44n9vdbmda.cloudfront.net/assets/x-ov-06-v1/sceneManipulator2Intro.mp4" type="video/mp4">
 </video>

 <video width="560" height="315" controls>
<source src="https://d36m44n9vdbmda.cloudfront.net/assets/x-ov-06-v1/sceneManipulator2.mp4" type="video/mp4">
 </video>
  
### Step 5: Find your Work Files

#### <b>Step 5.1: Open Visual Studio</b>

Go to the `Extensions` tab.

Click the `Widget Info` extension to open the extension overview to the right. 

Click the `VS Code` icon next to the folder icon:

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/vsCodeIcon.PNG?raw=true)

<br>

`VS Code` will pop up separately and look like this:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/vsCodeopened.png?raw=true)

<br>


#### <b>Step 5.2: Locate Manipulator Script</b>

Locate the files you need for this session in the left column drop-down menus at:

 `exts -> omni.example.ui_scene.widget_info\omni\example\ui_scene\widget_info`

You are working in

`widget_info_manipulator.py`

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/fileStructLocation.gif?raw=true)

<br>

### Step 6: Fix the Broken Slider
>#### Step 6.1: Add a New Import

Locate the `imports` at the top of the script.

Add the new import:

```python
from pxr import Gf
```

The imports will now look like this:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/newImport.png?raw=true)

<br>

In the following steps, you will use `Graphics Foundation`, or Gf, which is a package of fundamental graphics types and operations.

#### <b>Step 6.2: Find the Function Update_Scale</b>

Locate the following function at the bottom of the script:

```python
         # Update the slider
        def update_scale(prim_name, value):
```

This function updates the slider in the Widget. However, it currently does not have any logic to update the scale. Let's start adding the code we need to get that working!

#### <b>Step 6.3: Get the Current Stage</b>

Inside of `update_scale` function, find the `print` call.

Define the `stage` variable underneath this call, like so:

```python
            stage = self.model.usd_context.get_stage()
```

From the USD context we grab the active stage and store it into the stage variable. 

The `Stage` is where your prims are nested in the hierarchy. 


So now, `update_scale` should look like this:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/GetStage.png?raw=true)

<br>

><span>&#10071;</span> Make sure your new stage variable is lined up with the print call. If it is not, add or delete tabs until it is.

<br>

#### <b>Step 6.4: Get the Selected Prim</b>

Next, add a variable underneath the stage variable for the currently selected prim:

```python
            prim = stage.GetPrimAtPath(self.model._current_path)
```

`update_scale` will now look like this:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/getPrim.png?raw=true)

><span>&#10071;</span> This prim variable should be lined up with the stage and print call above it.

<br>

#### <b>Step 6.5: Update the Scale </b>

Add a new scale variable on the next line.

 In this variable you will get the scale `attribute` of the `xform` and the scale's Vector3 value, like so:

```python
            scale = prim.GetAttribute("xformOp:scale")
            scale.Set(Gf.Vec3d(value, value, value))
```

Now, your completed `update_scale` function will look like this:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/setScale.png?raw=true)

><span>&#10071;</span>The scale variable should be lined up with the variables above it.

<br>

### Step 7: Did it work?
#### <b>Step 7.1: Save and Test! </b>

Save your manipulator script and check that the scale slider works in your widget! 

><span>&#10071;</span> When you save, you may notice that the widget disappears in the viewport. This is to be expected, click the prim again to show the widget. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/scaleWorking.gif?raw=true)

Your slider is now being udpated by the function `update_scale`, where you added properties that grab the `Stage` and the currently selected `prim` that the widget is displayed on, then calls the scale vector3 when the slider is moved to scale the prim in all directions.

><span>&#10071;</span> Not Working? Check the `Console` to debug any errors.
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/Console.png?raw=true)

<br>

>#### :bell:<b>Challenge Step 8: Scale Larger</b>
><i>All Challenges in this workshop are optional</i>
>
>Can you change the function to scale the prim larger than 1.0?
>
><details>
><summary> Click here for the answer </summary>
>
>Set a `value` variable and multiply a number by value. 
>
>For example:
>
>```python
>        def update_scale(prim_name, value):
>            if value <= 0:
>                value = 0.01
>            print(f"changing scale of {prim_name}, {value}")
>            ## NEW VALUE VARIABLE ADDED BELOW
>            value = 10*value
>            stage = self.model.usd_context.get_stage()
>            prim = stage.GetPrimAtPath(self.model._current_path)
>            scale = prim.GetAttribute("xformOp:scale")
>            scale.Set(Gf.Vec3d(value, value, value))
>        if self._slider_model:      
>            self._slider_subscription = None
>            self._slider_model.as_float = 1.0
>            self._slider_subscription = self._slider_model.subscribe_value_changed_fn(
>                lambda m, p=self.model.get_item("name"): update_scale(p, m.as_float)
>            )
>```
>
></details>

<br>

>#### <span>&#129504;</span><b>Challenge Step 9: What other properties might you want to control with the widget?</b>
><i>All Challenges in this workshop are optional</i>
>
> Brainstorm 3-5 other properties that you could add to this widget. We will have an open discussion later on.

<br>

>### <span>&#9940;</span> Stop here and wait to move on to Section III

<br>

## Section III:
 
 <video width="560" height="315" controls>
<source src="https://d36m44n9vdbmda.cloudfront.net/assets/x-ov-06-v1/sceneManipulator3.mp4" type="video/mp4">
 </video>
  
### Step 10: Create your scene

#### <b>Step 10.1: Scale Everything!</b>

Play around in your scene and scale the prims in various sizes, such as a very large marble or a tiny jar. 

How can you make your scene unique?

><span>&#11088;</span> Press the `Play` button when you are finished!
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/playButton.png?raw=true)

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/section3.gif?raw=true)

<br>

>#### <span>&#129504;</span><b>Challenge Step 11: Scale in One Axis</b>
><i>All Challenges in this workshop are optional</i>
>
>Can you change the function to scale the prim in only one axis?
>
><details>
><summary> Click here for the answer </summary>
>
>Change the value's to 1 in `scale.Set(Gf.Vec3d(value,value,value))` of the axes that you do not want to scale in.  
>
>For example:
>
>```python
>scale.Set(Gf.Vec3d(value,1,1))
>```
>
>Which, would change the scale in the X axis as the Y and Z axis will remain at a value of 1 and the X axis will change.
>
></details>

<br>

>#### <span>&#129504;</span><b>Challenge Step 12: Turn on the Light Manipulator</b>
><i>All Challenges in this workshop are optional</i>
>
>Turn on the Light Manipulator Extension and click on the Rect Light.
>
>How can you change the intensity of the light using the tool?
>
><details>
><summary>Click here for the answer</summary>
>
>In the `Extensions` tab, search for Light in the `Community` and install/enable the `Omni.Ui Scene Sample for Manipulating Select Light` extension.
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/LightExt.png?raw=true)
>
><br>
>
>Select one of the Rect Lights in the hierarchy. 
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/RectLight.png?raw=true)
>
><br>
>
>Use your cursor to grab the edges of the Light tool and change the intensity by dragging forward or backward.
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/RectIntensity.png?raw=true)
>
></details>

<br>


## Congratulations!
You have completed this workshop! We hope you have enjoyed learning and playing with Omniverse! 

[<img src="https://developer-blogs.nvidia.com/wp-content/uploads/2022/07/ov-dev-contest-610x345-1.jpg">](https://www.nvidia.com/en-us/omniverse/apps/code/developer-contest/)

[Join us on Discord to extend the conversation!](https://discord.gg/BVFQEeXe)
