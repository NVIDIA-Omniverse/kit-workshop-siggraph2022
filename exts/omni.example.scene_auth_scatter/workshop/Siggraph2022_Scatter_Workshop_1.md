![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/logo.png?raw=true)
 
# NVIDIA OMNIVERSE

# Easily Develop Advanced 3D Layout Tools on NVIDIA Omniverse
 
See how to easily create your own custom scene layout tool with the modular Omniverse platform with a few lines of Python script. In this workshop, you'll build your own custom scene layout in Omniverse using Python.
 
# Learning Objectives
- How to Enable an extension
- Utilize Command Executions
- Create a feature to Scatter from a Prim's origin
 
<video width="560" height="315" controls> 
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1/3DLayoutToolsIntro.mp4" type="video/mp4">
</video>
 
# Section I

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1/3DLayoutToolsSection1.mp4" type="video/mp4">
</video>
 
# Open Stage and Get Extension from Community

## Step 1: Open the Workshop Stage

### <b>Step 1.1: Download the Stage from the Link Provided</b>

[Stage Link](https://dli-lms.s3.amazonaws.com/assets/x-ov-05-v1/Stage.zip)

### <b> Step 1.2: Unzip Stage Using Extract All...

This creates an unzipped file folder called `Stage`.

### <b> Step 1.3: Open Stage in Omniverse

Navigate inside Omniverse Code's `Content tab` to the stage file's location on your system.
  
(i.e. C:/Users/yourName/Downloads/Stage)
 
**Double Click** `Siggraph2022_Stage.usd` in the center window pane of the `Content tab` at the bottom of the Omniverse Code Console and it will appear in the viewport.
 
## Step 2: Adding the Extension

We will be getting an extension from the *Community Section* of the *Extension Manager*. There are also other extensions developed by NVIDIA in the *NVIDIA Section*.
 
### Step 2.1: Open Extension Manager
**Click** on the *Extension Tab*. 
 
### Step 2.2: Filter by Community Extensions
**Select** *Community* tab.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/filtercommunity.png?raw=true)

*Community* section is where you can find other developer's extensions from the Community. 

### Step 2.3: Search for Scatter
**Search** for "scatter" and **Click** on the extension with the subtitle *omni.example.scene_auth_scatter*.

> **Note:** There are two different scatter tools. Please double check that the one installed has the subtitle: *omni.example.scene_auth_scatter*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/communitysearch.png?raw=true)

### Step 2.4: Install/Enable the Extension
**Click** on the *Install button* to download the extension. If the extension is already downloaded **Click** on the toggle next to *Disable*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/installext.png?raw=true)

## Step 3: Using the Extension

With the extension enabled, try the following steps.

### Step 3.1: Select a Prim

Select a Prim in the *Stage* 

> **Note:** Prim is short for “primitive”, the prim is the fundamental unit in Omniverse. Anything imported or created in a USD scene is a prim. This includes, cameras, sounds, lights, meshes, and more. Primitives are technically containers of metadata, properties, and other prims. Read more about USD prims in the official documentation. 

We recommend using any of these Prims:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/primstoselect.png?raw=true)

#### Step 3.2: Set Prim Path to Scatter Window
With the selected Prim, **click** the *S button* in the *Scatter Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

#### Step 3.3: Scatter Selected Prim
At the bottom of the *Scatter Window*, **click** the *Scatter button*

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

### Step 3.4: Undo Scatter

Find the `Scatter01` folder in `Stage` and left-click on the folder then right-click to delete or hit the `delete` button on your keyboard. 

`Stage` is the panel that allows you to see all the assets in your current `USD`, or Universal Scene Description. It lists the prims in heirarchical order.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_3/exts/omni.example.ui_scatter_tool/Workshop/images/deletescatter.gif?raw=true)


  
## Challenge Step 4: What else can you do with the Scatter Extension
These are *optional* challenges. 

### Challenge 4.1: Use Cases
Come up with 5 use cases on how you would expand this extension. 


### Challenge 4.2: Scatter Multiple Prims at Once
Try to scatter more than one marble at once.

<details>
<summary>Hint</summary>

#### Challenge Step 4.2.1: Scatter Multiple Prims at Once
In the *Stage*, **hold** *Ctrl key* and **select** multiple Prims. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/multiprim.png?raw=true)

#### Challenge Step 4.2.2: Scatter Multiple Prims at Once
**Repeat** steps `3.2` and `2.3`.

</details>


# Section II

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1/3DLayoutToolsSection2Intro.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1/3DLayoutToolsWorkshop2.mp4" type="video/mp4">
</video>
 
# Scatter Relative to Source Prim
 
## Step 5: Change the Scatter functionality to Handle any Given Origin

To use any origin we will be modifying the scatter functionality to recieve a position. The current scatter tool sets scatter at world origin (0,0,0). This is inconvient when there are prims far away from origin.

### Step 5.1: Open the Extension in Visual Studio Code
From the *Scatter Extension*, **Click** the Visual Studio Icon.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/open_vs.png?raw=true)

A new instance of *Visual Studio Code* will open up.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/vs_code.png?raw=true)
 
### Step 5.2: Open `scatter.py`
**Locate** and **Open** `scatter.py` from `exts/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > scatter.py`

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterpy.png?raw=true)

### Step 5.3: Add New Origin Parameter to `scatter()`
**Add** `source_prim_location: List[float] = (0,0,0)` as a parameter for `scatter()`

``` python
def scatter(
    count: List[int],
    distance: List[float],
    randomization: List[float],
    id_count: int = 1,
    seed: Optional[int] = None,
    source_prim_location: List[float] = (0,0,0)
):
```
`source_prim_location` will contain x, y, and z coordinates of the prim we selected to scatter. 
 
### Step 5.4: Locate `result.SetTranslate`

**Locate** near the bottom of `scatter.py` the code snippet below.
``` python
result.SetTranslate(
    Gf.Vec3d(
        x,
        y,
        z,
    )
)
```

`Vec3d` creates a 3 dimensional vector. Each prim's position is generated via the code above.

### Step 5.5: Calculate the New Origin
During `Vec3d` creation, **add** each coordinate value stored in `source_prim_location` to the generated coordinate. i.e. `x` would turn into `source_prim_location[0] + x`.

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + x,
        source_prim_location[1] + y,
        source_prim_location[2] + z,
    )
)
```

`scatter()` should look as follows:

``` python 
def scatter(
    count: List[int],
    distance: List[float],
    randomization: List[float],
    id_count: int = 1,
    seed: Optional[int] = None,
    source_prim_location: List[float] = (0,0,0)
):
    """
    Returns generator with pairs containing transform matrices and ids to
    arrange multiple objects.

    ### Arguments:

        `count: List[int]`
            Number of matrices to generage per axis

        `distance: List[float]`
            The distance between objects per axis

        `randomization: List[float]`
            Random distance per axis

        `id_count: int`
            Count of differrent id

        `seed: int`
            If seed is omitted or None, the current system time is used. If seed
            is an int, it is used directly.

    """
    # Initialize the random number generator.
    random.seed(seed)

    for i in range(count[0]):
        x = (i - 0.5 * (count[0] - 1)) * distance[0]

        for j in range(count[1]):
            y = (j - 0.5 * (count[1] - 1)) * distance[1]

            for k in range(count[2]):
                z = (k - 0.5 * (count[2] - 1)) * distance[2]

                # Create a matrix 
                result = Gf.Matrix4d(1)
                result.SetTranslate(
                    Gf.Vec3d(
                        source_prim_location[0] + x,
                        source_prim_location[1] + y,
                        source_prim_location[2] + z,
                    )
                )

                id = int(random.random() * id_count)

                yield (result, id)
```

### Step 5.6: Save `scatter.py` and Open `window.py`  
**Save** `scatter.py` and **Open** `window.py` from `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > window.py`. 


![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/windowpy.png?raw=true)


### Step 5.7: Add Gf module
Underneath the imports and above `LABEL_WIDTH`, **add** the line `from pxr import Gf`

``` python
import omni.ui as ui
from .style import scatter_window_style
from .utils import get_selection
from .combo_box_model import ComboBoxModel
from .scatter import scatter
from .utils import duplicate_prims
from pxr import Gf

LABEL_WIDTH = 120
SPACING = 4
```

### Step 5.8: Locate `transforms`

**Locate** where `transforms` is declared inside of `_on_scatter()`

``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int
)
```

### Step 5.9 Hard Code Origin Position

**Add** `source_prim_location=Gf.Vec3d((0,0,-500))`after `seed=self._scatter_seed_model.as_int`. 

>**Note:** Don't forget to add a comma after `seed=self._scatter_seed_model.as_int`.

``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int,
    source_prim_location=Gf.Vec3d((0,0,-500))
)
```

`Gf.Vec3d((0,0,-500))` creates a 3 coordinate vector where x = 0, y = 0 and z = -500. Since Y represents up and down in the scene, X and Z are like a floor. By setting Z to -500 we are setting the scatter location -500 units along the Z axis.  

### Step 5.10: Select a Marble in the *Stage* 
**Save** `window.py` and go back to *Omniverse Code*. Go to *Stage* and **expand** Marbles, then **select** any marble. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleselect.png?raw=true)
 
### Step 5.11: Set the Selected Marble's Path to the Scatter Extension
With a marble selected, **click** on the *S button* in the *Scatter Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

### Step 5.12: Scatter the Marbles
**Scroll** to the bottom of the extension and **click** the *Scatter button*.
> **Note**: If you do not see the *Scatter button* **scroll down** in the *extension window* or **expand** the *extension window* using the right corner. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

Notice how the marbles scattered to the right of the stage. This is -500 units on the Z axis. Try and change some of the values in the Y and/or X axis as well to see where the marbles will scatter next.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/sidescatter.png?raw=true)

 
## Step 6: Get the Location of the Source Prim

We will be changing the origin where the Prims get scattered. Firstly, we will be grabbing the location of the source prim.
 
### Step 6.1: Open `window.py`
**Open** `window.py` from `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > window.py`

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/windowpy.png?raw=true)


### Step 6.2: Add `omni.usd` module
Under `import omni.ui as ui`, **add** the line `import omni.usd`

``` python
# Import omni.usd module
import omni.usd
```
You should then have the following at the top of your file:
``` python
import omni.ui as ui
import omni.usd
from .style import scatter_window_style
from .utils import get_selection
from .combo_box_model import ComboBoxModel
from .scatter import scatter
from .utils import duplicate_prims
from pxr import Gf
```

The `omni.usd` module is one of the core Kit APIs, and provides access to USD (Universal Scene Description) and USD-related application services.

### Step 6.3: Locate `_on_scatter()`
**Scroll Down** to find `_on_scatter()`, and **add** a new line before the variable declaration of `transforms`.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/newline.png?raw=true)

`_on_scatter()` is called when the user presses the *Scatter* button in the extension window.

### Step 6.4: Get USD Context
 
On the new line, **declare** `usd_context`. Make sure the line is tabbed in and parallel with the line `if not prim_names:`.

``` python
usd_context = omni.usd.get_context()
```

Your code should look like the following:

``` python
def _on_scatter(self):
    """Called when the user presses the "Scatter" button"""
    prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
    if not prim_names:
        prim_names = get_selection()

    if not prim_names:
        # TODO: "Can't clone" message
        pass

    # Get the UsdContext we are attached to
    usd_context = omni.usd.get_context()

    transforms = scatter(
        count=[m.as_int for m in self._scatter_count_models],
        distance=[m.as_float for m in self._scatter_distance_models],
        randomization=[m.as_float for m in self._scatter_random_models],
        id_count=len(prim_names),
        seed=self._scatter_seed_model.as_int,
    )

    duplicate_prims(
        transforms=transforms,
        prim_names=prim_names,
        target_path=self._scatter_prim_model.as_string,
        mode=self._scatter_type_model.get_current_item().as_string,
    )
```    
 
### Step 6.5: Get the Stage 
Below `usd_context` declaration, **add** `stage = usd_context.get_stage()`

``` python
# Store the UsdContext we are attached to
usd_context = omni.usd.get_context()
# Get the stage from the current UsdContext
stage = usd_context.get_stage() 
```

The stage variable will use USD to get the current stage. The `Stage` is where your prims are nested in the hierarchy.

### Step 6.6: Get Source Prim from Stage 
On the next line, **add** `prim = stage.GetPrimAtPath(self._source_prim_model.as_string)`
``` python
# Store the UsdContext we are attached to
usd_context = omni.usd.get_context()
# Get the stage from the current UsdContext
stage = usd_context.get_stage() 
# Store the Prim that is currently referenced in the extension
prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
```

### Step 6.7: Get Source Prim's Translation

Next we will **store** the prim's positional data by adding, `position = prim.GetAttribute('xformOp:translate').Get()`. After checking your work below **save** `window.py`.

``` python
# Store the UsdContext we are attached to
usd_context = omni.usd.get_context()
# Get the stage from the current UsdContext
stage = usd_context.get_stage() 
# Store the Prim that is currently referenced in the extension
prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
# Get the focused Prim's positional data
position = prim.GetAttribute('xformOp:translate').Get() 
```

In order to get the location of the prim, we needed the translate value which is stored in the Xform. This gives us a X, Y, and Z of the selected prim.

> **Note** The Transform (Xform) is the fundamental element of all objects in Omniverse, the Location.

Check your work, it should look like this:

``` python
def _on_scatter(self):
    """Called when the user presses the "Scatter" button"""
    prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
    if not prim_names:
        prim_names = get_selection()

    if not prim_names:
        # TODO: "Can't clone" message
        pass

    # Store the UsdContext we are attached to
    usd_context = omni.usd.get_context()
    # Get the stage from the current UsdContext
    stage = usd_context.get_stage() 
    # Store the Prim that is currently referenced in the extension
    prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
    # Get the focused Prim's positional data
    position = prim.GetAttribute('xformOp:translate').Get() 

    transforms = scatter(
        count=[m.as_int for m in self._scatter_count_models],
        distance=[m.as_float for m in self._scatter_distance_models],
        randomization=[m.as_float for m in self._scatter_random_models],
        id_count=len(prim_names),
        seed=self._scatter_seed_model.as_int,
        source_prim_location=Gf.Vec3((0,0,-500))
    )

    duplicate_prims(
        transforms=transforms,
        prim_names=prim_names,
        target_path=self._scatter_prim_model.as_string,
        mode=self._scatter_type_model.get_current_item().as_string,
    )
```
 

 
## Step 7: Use the Selected Prim's Location as the Scatter Origin

After updating the scatter functionality we can pass the location of the source prim that we calculated from before.
 
### Step 7.1: Open window.py
**Open** `window.py` and locate where `transforms` is declared in `_on_scatter()`

``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int
)
```
 
### Step 7.2: Pass the Location to `scatter()`
After `seed=self._scatter_seed_model.as_int`, **replace** the line `source_prim_location=Gf.Vec3d(0,0,-500)` with `source_prim_location=position`  


``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int,
    source_prim_location=position
)
```

### Step 7.3: Test it out
Save `window.py` and head back into Omniverse. **Scatter** a prim in the stage. Then **scatter** a different prim. Notice how they will only scatter to the corresponding prim's location. 

### Step 7.4: Hit Play
Play out the scene! 

## Challenge Step 8.1: Add Randomization to Scatter
Currently, when the *Scatter button* is pressed it will scatter uniformly. Try to change up the code to allow for random distrubtion. Expand the *Hint* section if you get stuck.

> **Hint** Use `random.random()`

<details>
<summary>Hint</summary>

### Challenge Step 8.1.1: Open `scatter.py`

**Open** `scatter.py` and *locate* `scatter()`.

 
### Challenge Step 8.1.2: Add Random Value
**Locate** where we generate our Vec3d / `result.SetTranslate()`. **Modify** the first passed parameter as `source_prim_location[0] + (x + random.random() * randomization[0]),`

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + (x + random.random() * randomization[0]),
        source_prim_location[1] + y,
        source_prim_location[2] + z,
    )
)
```

`randomization[0]` refers to the element in the UI of the *Scatter Extension Window* labeled *Random*.

### Challenge Step 8.1.3: Apply to Y and Z Values
**Modify** the Y and Z values that get passed into *Vec3d* constructor similar to the previous step.

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + (x + random.random() * randomization[0]),
        source_prim_location[1] + (y + random.random() * randomization[1]),
        source_prim_location[2] + (z + random.random() * randomization[2]),
    )
)
```

### Challenge Step 8.1.4: Change Random Value
**Save** `scatter.py` and **go back** to Omniverse. **Modify** the *Random* parameter in the *Scatter Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/random.png?raw=true)

### Challenge Step 8.1.5: Scatter Prims
**Click** the *Scatter button* and see how the Prims scatter.

> **Note:** Make your Random values high if you are scattering in a small area. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/randomscatter.png?raw=true)

 
</details>

<br>


# Section III

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1/3DLayoutToolsWorkshop3.mp4" type="video/mp4">
</video>
 
# Scatter the Objects
 
## Step 9: Scatter a Marble

The stage has a few marbles we can use to scatter around.
 
### Step 9.1: Select a Marble in the *Stage* 
Go to *Stage* and **expand** Marbles, then **select** any marble.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleselect.png?raw=true)
 
### Step 9.2: Copy the Selected Marble's Path to the Scatter Extension
With a marble selected, **click** on the *S button* in the *Scatter Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

### Step 9.3: Change Distance Value for X Axis
**Change** the *Distance* in the *X Axis* to 10.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/distance10.png?raw=true)

### Step 9.4: Click the Scatter Button
**Click** the *Scatter* button at the bottom of the window.
> **Note**: If you do not see the *Scatter button* **scroll down** in the *extension window* or **expand** the *extension window* using the right corner. 

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

Your scene should look similar to this after clicking the *Scatter button*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleScattered.png?raw=true)
 
## Step 10: Watch the Scene Play

The play button is used for more than playing animations or movies. We can also use the play button to simulate physics. 
 
### Step 10.1: Hit the Play Button
With the marbles scattered we can watch it in action. **Click** the *Play button* to watch the scene.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbutton.png?raw=true)
 
What happens when we press play:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbuttonaction.gif?raw=true)

> **Note:** To reset the scene **click** the *Stop button*.

### Step 10.2: Select a Different Prim
**Select** a diferent Prim in the *Stage*. It could be another marble, the jar, bowl, etc.

We recommend using any of these Prims:

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/primstoselect.png?raw=true)

### Step 10.3: Copy Selected Prim to Scatter Window
With the Prim selected, **Click** the *S button* to copy the Prim Path into the *Scatter Extension Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)
 
### Step 10.4: Change Scatter Parameters
**Change** some of the parameters in the *Scatter Window*. I.e. In *Y Axis* **change** *Object Count* to 20 and *Distance* to 5.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/params.png?raw=true)

### Step 10.5: Scatter New Prims
**Click** the *Scatter button* at the bottom of the *Scatter Window*.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)
 
### Step 10.6: Hit the Play Button
**Click** the *Play button* and watch the scene play out.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbutton.png?raw=true)

Try to Scatter many items in the scene and play around with the extension.

## Challenge Step 11: Scale Scatter Prims based on Provided Scale

You will notice that there is a *Scale* option. However, this does not work. Try to get it working. Expand the *Hint* section if you get stuck.

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scale.png?raw=true)

> **Tip:** Look into `window.py` to see where the value get's used.

<details>
<summary>Hint</summary>

### Challenge Step 11.1: Locate `duplicate_prims()` in `window.py`
**Find** `duplicate_prims()` in `window.py`.

``` python
duplicate_prims(
    transforms=transforms,
    prim_names=prim_names,
    target_path=self._scatter_prim_model.as_string,
    mode=self._scatter_type_model.get_current_item().as_string
)
```
`duplicate_prims()` will take all of the transforms and depending on the mode selected duplicate's the selected prim. This is ideal for adding in a scale parameter. 

### Challenge Step 11.2: Pass Scale values in `duplicate_prims()`
`self._scale_models` holds each scale set in the *Scatter Window*. **Add** `scale=[self._scale_models[0].as_float, self._scale_models[1].as_float, self._scale_models[2].as_float]` in `duplicate_prims()`.

``` python
duplicate_prims(
    transforms=transforms,
    prim_names=prim_names,
    target_path=self._scatter_prim_model.as_string,
    mode=self._scatter_type_model.get_current_item().as_string,
    scale=[self._scale_models[0].as_float, self._scale_models[1].as_float, self._scale_models[2].as_float]
)
```

### Challenge Step 11.3: Locate `duplicate_prims()` in `utils.py`
**Open** `utils.py` from `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > utils.py`. **Locate** `duplicate_prims()`.

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy"):
```

### Challenge Step 11.4: Add new parameter to `duplicate_prims()`
**Add** `scale: List[float] = [1,1,1]` as a parmeter for `duplicate_prims()`.

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy", scale: List[float] = [1,1,1]):
```

### Challenge Step 11.5: Pass Scale Parameter into Kit Command
**Scroll down** to find `omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform)`
**Add** `new_scale=scale` to Kit Command.

``` python
omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform, new_scale=scale)
```
 
### Challenge Step 11.6: Save and Test
**Save** the files and try to Scatter Prims with a different scale.

![](images/scatterscale.gif)
![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterscale.gif?raw=true)
 
</details>

## Congratulations!
You have completed this workshop! We hope you have enjoyed learning and playing with Omniverse! 

[<img src="https://developer-blogs.nvidia.com/wp-content/uploads/2022/07/ov-dev-contest-610x345-1.jpg">](https://www.nvidia.com/en-us/omniverse/apps/code/developer-contest/)

[Join us on Discord to extend the conversation!](https://discord.gg/BVFQEeXe)
