![](images/logo.png)
 
# NVIDIA OMNIVERSE

# Easily Develop Advanced 3D Layout Tools on NVIDIA Omniverse
 
See how to easily create your own custom scene layout tool with the modular Omniverse platform with a few lines of Python script. In this workshop, you'll build your own custom scene layout in Omniverse using Python.
 
# Learning Objectives
- How to Enable an extension
- Utilize Command Executions
- Create a feature to Scatter from a Prim's origin
 
# Open Stage and Get Extension from Community
 
## Step 1: Prepare your Environment

### Step 1.1: Find Bookmarks tab

**Find** the *Content tab* at the bottom of Omniverse Code and **locate** the `Bookmarks` drop down.

### Step 1.2: Open Folder

In the dropdown, **locate** the `Siggraph2022_Stage` folder. 

**Open** the `Workshop_1` folder.

### Step 1.3: Open the Stage

**Open** `Siggraph2022_Stage.usd`

![](images/workshopstage.png#center)
 
## Step 2: Add the Extension
 
### Step 2.1: Open Extension Manager
**Click** on the *Extension Tab*. 
 
### Step 2.2: Filter by Community Extensions
**Select** *Community* tab.

![](images/filtercommunity.png)

*Community* section is where you can find other developer's extensions from the Community. 

### Step 2.3: Search for Scatter
**Search** for "scatter" and **Click** on *Omni.ui Window Scatter*.

![](images/communitysearch.png#center)

### Step 2.4: Install/Enable the Extension
**Click** on the *Install button* to download the extension. If the extension is already downloaded **Click** on the toggle next to *Disable*.

![](images/installext.png#center)
  
## Challenge Step 3: Using the Scatter Extension

With the extension enabled, try using it. Come up with 5 use cases on how you would expand this extension. Use the *Challenge Steps* below to check your answer.

<details>
<summary>Challenge Steps</summary>

### Challenge Step 3.1: Select a Prim

Select a Prim in the *Stage* 
We recommend using any of these Prims:

![](images/primstoselect.png)

### Challenge Step 3.2: Copy Prim Path to Scatter Window
With the selected Prim, **click** the *S button* in the *Scatter Window*.

![](images/clickS.png)

### Challenge Step 3.3: Scatter Selected Prim
At the bottom of the *Scatter Window*, **click** the *Scatter button*

![](images/scatterbutton.png)

### Challenge Step 3.4: Scatter Multiple Prims at Once
In the *Stage*, **hold** *Ctrl key* and **select** multiple Prims. 

![](images/multiprim.png)

### Challenge Step 3.5: Scatter Multiple Prims at Once
**Repeat** steps `3.2` and `3.3`.

### Challenge Step 3.6: Scatter Prims Close Together
To Scatter Prims closer together, **adjust** the *Distance* value in the *Scatter Window*.

![](images/distance10.png)


### Challenge Step 3.7: Scatter Less or More Prims
To change the amount of Prims that will instantiate, **adjust** the *Object Count* value in the *Scatter Window*.

![](images/objcount.png)
 
</details>
 
<br>
 
# Scatter Relative to Source Prim
 
## Step 1: Update window.py
 
### Step 1.1: Open the Extension in Visual Studio Code
From the *Scatter Extension*, **Click** the Visual Studio Icon.

![](images/open_vs.png#center)

A new instance of *Visual Studio Code* will open up.

![](images/vs_code.png#center)

### Step 1.2: Open `window.py`
**Open** `window.py` from `ext/omni.example.ui_scatter_tool > omni/example/ui_scatter_tool > window.py`

![](images/windowpy.png#center)


### Step 1.3: Add `omni.usd` module
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
```


### Step 1.4: Locate `_on_scatter()`
**Scroll Down** to find `_on_scatter()`, and **add** a new line before the variable declaration of `transforms`.

``` python
def _on_scatter(self):
    """Called when the user presses the "Scatter" button"""
    prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
    if not prim_names:
        prim_names = get_selection()

    if not prim_names:
        # TODO: "Can't clone" message
        pass

    # ADD NEW LINE HERE

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
`_on_scatter()` is called when the user presses the *Scatter* button in the extension window.

### Step 1.5: Get USD Context
 
On the new line, **declare** `usd_context`

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
 
### Step 1.6: Get the Stage 
Below `usd_context` declaration, **add** `stage = usd_context.get_stage()`

``` python
# Store the UsdContext we are attached to
usd_context = omni.usd.get_context()
# Get the stage from the current UsdContext
stage = usd_context.get_stage() 
```

### Step 1.7: Get Source Prim from Stage 
On the next line, **add** `prim = stage.GetPrimAtPath(self._source_prim_model.as_string)`
``` python
# Store the UsdContext we are attached to
usd_context = omni.usd.get_context()
# Get the stage from the current UsdContext
stage = usd_context.get_stage() 
# Store the Prim that is currently referenced in the extension
prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
```

### Step 1.8: Get Source Prim's Translate 
Using `prim`, **store** it's positional data by adding, `position = prim.GetAttribute('xformOp:translate1).Get()`.
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
The complete code for `_on_scatter()` is the following:
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
    )

    duplicate_prims(
        transforms=transforms,
        prim_names=prim_names,
        target_path=self._scatter_prim_model.as_string,
        mode=self._scatter_type_model.get_current_item().as_string,
    )
```
 
## Step 2: Update `scatter()`
 
### Step 2.1: Open `scatter.py`
**Locate** and **Open** `scatter.py` from `exts/omni.example.ui_scatter_tool > omni/example/ui_scatter_tool > scatter.py`

![](images/scatterpy.png#center)

### Step 2.2: Add New Parameter to `scatter()`
**Add** `source_prim_location: List[float] = (0,0,0)` as a parameter for `scatter()`

``` python
def scatter(
    count: List[int], distance: List[float], randomization: List[float], id_count: int = 1, seed: Optional[int] = None, source_prim_location: List[float] = (0,0,0)
):
```
`source_prim_location` will contain x, y, and z coordinates of the prim we selected to scatter. 
 
### Step 2.3: Update Vec3d Creation
During `Vec3d` creation, **add** each coordinate value stored in `source_prim_location` to the generated coordinate.

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
    count: List[int], distance: List[float], randomization: List[float], id_count: int = 1, seed: Optional[int] = None, source_prim_location: List[float] = (0,0,0)
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

 
## Step 3: Pass Position into `scatter()`, in `window.py`
 
### Step 3.1: Open window.py
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
 
### Step 3.2: Add the Variable position to `scatter()`
After `seed=self._scatter_seed_model.as_int`, **add** a comma then on a new line **add** the line `source_prim_location=position`


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

## Challenge Step 4: Add Randomization to Scatter
Currently, when the *Scatter button* is pressed it will scatter uniformly. Try to change up the code to allow for random distrubtion. Use the *Challenge Steps* below to check your answer.

> **Hint** Use `random.random()`

<details>
<summary>Challenge Steps</summary>

### Challenge Step 4.1: Open `scatter.py`

**Open** `scatter.py` and *locate* `scatter()`.

 
### Challenge Step 4.2: Add Random Value
**Locate** where we generate our Vec3d. **Modify** the first passed parameter as `source_prim_location[0] + (x + random.random() * randomization[0]),`

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

### Challenge Step 4.3: Apply to Y and Z Values
**Modify** the Y and Z values that get passed into *Vec3d* constructor similar to the previous step.

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + (x + random.random() * randomization[0]),
        source_prim_location[1] + (y + random.random() * randomization[1],
        source_prim_location[2] + (z + random.random() * randomization[2],
    )
)
```

### Challenge Step 4.4: Change Random Value
**Go back** to Omniverse and **modify** the *Random* parameter in the *Scatter Window*.

![](images/random.png#center)

### Challenge Step 4.5: Scatter Prims
**Click** the *Scatter button* and see how the Prims scatter.

> **Note:** Make your Random values high if you are scattering in a small area. 

![](images/scatterbutton.png#center)

![](images/randomscatter.png#center)

 
</details>

<br>

# Scatter the Objects
 
## Step 1: Scatter a Marble
 
### Step 1.1: Select a Marble in the *Stage* 
Go to *Stage* and **expand** Marbles, then **select** any marble.

![](images/marbleselect..png#center)
 
### Step 1.2: Copy the Selected Marble's Path to the Scatter Extension
With a marble selected, **click** on the *S button* in the *Scatter Window*.

![](images/clickS.png#center)

### Step 1.3: Change Distance Value for X Axis
**Change** the *Distance* in the *X Axis* to 10.

![](images/distance10.png#center)

### Step 1.4: Click the Scatter Button
**Click** the *Scatter* button at the bottom of the window.
> **Note**: If you do not see the *Scatter button* **scroll down** in the *extension window* or **expand** the *extension window* using the right corner. 

![](images/scatterbutton.png#center)

Your scene should look similar to this after clicking the *Scatter button*.

![](images/marbleScattered.png#center)
 
## Step 2: Watch the Scene Play
 
### Step 2.1: Hit the Play Button
With the marbles scattered we can watch it in action. **Click** the *Play button* to watch the scene.

![](images/playbutton.png#center)
 
What happens when we press play:

![](images/playbuttonaction.gif)

> **Note:** To reset the scene **click** the *Stop button*.

### Step 2.2: Select a Different Prim
**Select** a diferent Prim in the *Stage*. It could be another marble, the jar, bowl, etc.

We recommend using any of these Prims:

![](images/primstoselect.png)

### Step 2.3: Copy Selected Prim to Scatter Window
With the Prim selected, **Click** the *S button* to copy the Prim Path into the *Scatter Extension Window*.

![](images/clickS.png)
 
### Step 2.4: Change Scatter Parameters
**Change** some of the parameters in the *Scatter Window*. I.e. In *Y Axis* **change** *Object Count* to 20 and *Distance* to 5.

![](images/params.png)

### Step 2.5: Scatter New Prims
**Click** the *Scatter button* at the bottom of the *Scatter Window*.

![](images/scatterbutton.png)
 
### Step 2.6: Hit the Play Button
**Click** the *Play button* and watch the scene play out.

![](images/playbutton.png)

Try to Scatter many items in the scene and play around with the extension.

## Challenge Step 3: Scale Scatter Prims based on Provided Scale

You will notice that there is a *Scale* option. However, this does not work. Try to get it working. Use the Challenge Steps below to check your answer.

![](images/scale.png)

> **Tip:** Look into `window.py` to see where the value get's used.

<details>
<summary>Challenge Steps</summary>

### Challenge Step 3.1: Locate `duplicate_prims()` in `window.py`
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

### Challenge Step 3.2: Pass Scale values in `duplicate_prims()`
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

### Challenge Step 3.3: Locate `duplicate_prims()` in `utils.py`
**Open** `utils.py` from `ext/omni.example.ui_scatter_tool > omni/example/ui_scatter_tool > utils.py`. **Locate** `duplicate_prims()`.

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy"):
```

### Challenge Step 3.4: Add new parameter to `duplicate_prims()`
**Add** `scale: List[float] = [1,1,1]` as a parmeter for `duplicate_prims()`.

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy", scale: List[float] = [1,1,1]):
```

### Challenge Step 3.5: Pass Scale Parameter into Kit Command
**Scroll down** to find `omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform)`
**Add** `new_scale=scale` to Kit Command.

``` python
omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform, new_scale=scale)
```
 
### Challenge Step 3.6: Save and Test
**Save** the files and try to Scatter Prims with a different scale.

![](images/scatterscale.gif)
 
</details>

## Congratulations!
You have completed this workshop! We hope you have enjoyed learning and playing with Omniverse! 

[Join us on Discord to extend the conversation!](https://discord.gg/BVFQEeXe)