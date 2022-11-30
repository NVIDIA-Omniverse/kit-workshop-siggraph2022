
![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/logo.png?raw=true)
 
# NVIDIA OMNIVERSE

# 通过 NVIDIA Omniverse 轻松开发高级 3D 设计工具
 
了解如何仅借助数行 Python 脚本，通过模块化 Omniverse 平台轻松创建您自己的自定义场景布局工具。在本课程中，您将在 Omniverse 中使用 Python 构建您的自定义场景布局。
 
# 学习目标
- 了解如何启用扩展功能
- 使用命令执行
- 创建一个从基元的原点散布对象的功能
 
<video width="560" height="315" controls> 
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1-zh/3DLayoutToolsIntro_CN_v1.mp4" type="video/mp4">
</video>
 
# 第 I 部分 打开 Stage，并从社区（或第三方）获取扩展功能

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1-zh/3DLayoutToolsSection1_CN_v1.mp4" type="video/mp4">
</video>
 
## 第 1 步：打开 Workshop Stage

### <b>第 1.1 步：从下面提供的链接下载 Stage </b>

[下载 Stage](https://dli-lms.s3.amazonaws.com/assets/x-ov-05-v1/Stage.zip)

### <b>第 1.2 步：使用 “Extract All...”（提取所有文件...）解压 Stage </b>

此操作会创建一个名为 `Stage` 的解压文件夹。

### <b>第 1.3 步：在 Omniverse 中打开 Stage </b>

在 Omniverse Code 的 `Content`（内容）选项卡中，找到系统中存放 Stage 文件的位置。
  
（即 C:/Users/yourName/Downloads/Stage）
 
在 Omniverse Code 控制台底部的 `Content` （内容）选项卡中，**双击**中间窗格中的 `Stage.usd`，即可在视图区中打开该 Stage。

 
## 第 2 步：添加扩展功能

我们将从“Extension Manager”（扩展功能管理器）的`Community/Third Party`（社区/第三方）部分获取扩展功能。此外，在`NVIDIA`部分可以获取 NVIDIA 开发的其他扩展功能。
 
### 第 2.1 步：打开 `Extensions`（扩展功能）选项卡
单击 `Extensions`（扩展功能）管理器选项卡
 
### 第 2.2 步：对来自社区或第三方的扩展功能进行筛选
选择 `Community/Third Party`（社区/第三方）选项卡
<br>
![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/filtercommunity.png?raw=true)

在`Community/Third Party`（社区/第三方）部分，您可以找到由社区中的其他开发者提供的扩展功能。

### 第 2.3 步：搜索 Scatter（散布）工具
在搜索框中搜索“scatter”，然后**单击**副标题为 *omni.example.scene_auth_scatter* 的扩展功能。

> **注意：**可以找到两个不同的 Scatter 工具。请仔细核对，确保您安装的 Scatter 工具的副标题为：*omni.example.scene_auth_scatter*。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/communitysearch.png?raw=true)

### 第 2.4 步：安装/启动扩展程序
**单击`Install`（安装）按钮，下载该扩展功能。如果您已经下载了该扩展功能，请单击`Disable`（禁用）旁边的切换按钮。**

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/installext.png?raw=true)

## 第 3 步：使用扩展功能

启用扩展功能后，请尝试执行以下步骤。

### 第 3.1 步：选择一个 Prim（基元）

在 Stage 中选择一个 prim。

> **注意：Prim（基元）是 primitive 的简写，它是 Omniverse 中的基本单元。在 USD 场景中导入或创建的任何对象，都是一个基元，例如镜头、声音、光线、网格等等。从技术角度看，Prim 是元数据、属性和其他基元的容器。您可以在官方文档中了解有关 USD 基元的更多的信息。**

我们建议使用下面圈出的任意基元：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/primstoselect.png?raw=true)

### 第 3.2 步：在 `Scatter Window`（散布窗口）中设置基元的路径
选择好基元后，**单击**`Scatter Window`（散布窗口）中的`S`按钮。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

### 第 3.3 步：使用选定的基元执行散布操作
在`Scatter Window`（散布窗口）底部，**单击** `Scatter`（散布）按钮。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

### 第 3.4 步：撤消散布操作

在 `Stage` 选项卡下面，找到 `Scatter01` 文件夹并左键单击该文件夹，然后单击鼠标右键选择“Delete”（删除）或按下键盘上的 `delete` 按钮，即可将其删除。

在 `Stage` 面板中，您可以看到当前 `USD` (Universal Scene Description) 中的所有素材。它会按层次顺序列出基元。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_3/exts/omni.example.ui_scatter_tool/Workshop/images/deletescatter.gif?raw=true)


  
## 第 4 步（自我挑战）：您还可以使用散布扩展功能执行哪些其他操作？
下面是*可选的*自我挑战。

### 第 4.1 步（自我挑战）：用例
通过 5 个用例了解如何进一步使用散布扩展功能。


### 第 4.2 步（自我挑战）：一次对多个基元执行散布操作
尝试一次对多个大理石基元执行散布操作。

<details>
<summary>提示</summary>

#### 第 4.2.1 步（自我挑战）：一次对多个基元执行散布操作
在`Stage`里，**按住** `Ctrl` 键**选择**多个基元。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/multiprim.png?raw=true)

#### 第 4.2.2 步（自我挑战）：一次对多个基元执行散布操作
**重复**第 `3.2` 步和第 `2.3` 步。

</details>


# 第 II 部分 相对于源基元的散布操作

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1-zh/3DLayoutToolsSection2Intro_CN_v1.mp4" type="video/mp4">
</video>

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1-zh/3DLayoutToolsWorkshop2_CN_v1.mp4" type="video/mp4">
</video>

## 第 5 步：更改散布功能，以支持任意给定的原点

要将散布功能用于任意原点，我们需要对其进行修改，使其能够接收位置数据。当前的散布工具将散布功能设置在 Stage 的原点 (0,0,0)。要是有一些基元位于距原点很远的位置，就会非常不便。

### 第 5.1 步：在 Visual Studio Code 中打开扩展功能
从 `Scatter Extension`（散布扩展功能）中，**单击** `Visual Studio` 图标。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/open_vs.png?raw=true)

系统将打开一个新的 *Visual Studio Code* 实例。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/vs_code.png?raw=true)
 
### 第 5.2 步：打开 `scatter.py`
在 `exts/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > scatter.py` 中，**找到**并**打开** `scatter.py`。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterpy.png?raw=true)

### 第 5.3 步：向 `scatter()` 添加新原点参数
**将** `source_prim_location: List[float] = (0,0,0)` 作为参数，添加到 `scatter()`

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
`source_prim_location` 将包含我们选定执行散布操作的prim（基元）的 x 轴、y 轴和 z 轴坐标。
 
### 第 5.4 步：找到 `result.SetTranslate`

在 `scatter.py` 的底部，**找到**如下代码片段。
``` python
result.SetTranslate(
    Gf.Vec3d(
        x,
        y,
        z,
    )
)
```

`Vec3d` 会创建一个三维向量。每个prim（基元）的位置都是通过上面这段代码生成的。

### 第 5.5 步：计算新原点
在 `Vec3d` 创建过程中，将 `source_prim_location` 中存储的各个坐标值**添加**到生成的坐标，例如：`x` 应改为 `source_prim_location[0] + x`。

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + x,
        source_prim_location[1] + y,
        source_prim_location[2] + z,
    )
)
```

`scatter()` 应类似下面的示例代码：

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
    使用包含变换矩阵和 ID 的数据对返回生成器，
    以排列多个对象。

    ### 参数：

        `count: List[int]`
            每个坐标轴上要生成的矩阵的数量

        `distance: List[float]`
            每个坐标轴上各个对象之间的距离

        `randomization: List[float]`
            每个坐标轴的随机距离

        `id_count: int`
            不同 ID 的数量

        `seed: int`
            如果不设置 seed 或将 seed 设置为“None”，则使用当前系统时间。如果将 seed
            设置为 int 类型，则直接使用它。

    """
    # 初始化随机数字生成器。
    random.seed(seed)

    for i in range(count[0]):
        x = (i - 0.5 * (count[0] - 1)) * distance[0]

        for j in range(count[1]):
            y = (j - 0.5 * (count[1] - 1)) * distance[1]

            for k in range(count[2]):
                z = (k - 0.5 * (count[2] - 1)) * distance[2]

                # 创建矩阵 
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

### 第 5.6 步：保存 `scatter.py` 并打开 `window.py`  
**保存** `scatter.py`，然后从 `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > window.py` **打开** `window.py`。


![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/windowpy.png?raw=true)


### 第 5.7 步：添加 Gf 模块
在导入代码部分，在 `LABEL_WIDTH` 的上方，**添加**一行代码：`from pxr import Gf`。

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

### 第 5.8 步：找到 `transforms`

**找到** `_on_scatter()` 中声明 `transforms` 的位置。

``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int
)
```

### 第 5.9 步：硬编码原点位置

在 `seed=self._scatter_seed_model.as_int` 后面，**添加** `source_prim_location=Gf.Vec3d((0,0,-500))`。

> **注意：**请别忘记在 `seed=self._scatter_seed_model.as_int` 后面添加逗号。

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

`Gf.Vec3d((0,0,-500))` 会创建一个三坐标向量，坐标值为 x = 0、y = 0、z = -500。由于 Y 值代表stage上下方向的坐标，所以 X 值和 Z 值相当于位于地面上。通过将 Z 值设置为 -500，即可将散布位置设置到沿 Z 轴移动 -500 单位的位置。

### 第 5.10 步：在*Stage*中选择一块大理石 
**保存** `window.py`，然后回到 *Omniverse Code*。转到*Stage*部分，**展开**“Marbles”（大理石），然后**选择**任意大理石素材。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleselect.png?raw=true)
 
### 第 5.11 步：在散布扩展中设置所选大理石的路径
选择好大理石素材后，**单击**`Scatter Window`（散布窗口）中的`S`按钮。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

### 第 5.12 步：对大理石执行散布操作
**滚动**到扩展功能的底部，然后**单击**`Scatter`（散布）按钮。
> **注意：**如果看不到`Scatter`（散布）按钮，请在*扩展程序窗口*中**向下滚动**，或者拉动右下角**扩大***扩展程序窗口*。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

注意观察大理石如何在Stage的右侧进行散布。该位置也就是 Z 轴上 -500 单位的位置。尝试更改 Y 轴和/或 X 轴的某些值，看看大理石会改在哪里进行散布。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/sidescatter.png?raw=true)

 
## 第 6 步：获取源 prim 的位置

在这一步中，我们将更改对 prim 执行散布操作的原点。首先，我们需要获取源 prim 的位置。
 
### 第 6.1 步：打开 `window.py`
从 `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > window.py` **打开** `window.py`

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/windowpy.png?raw=true)


### 第 6.2 步：添加 `omni.usd` 模块
在 `import omni.ui as ui` 下面，**添加**一行代码：`import omni.usd`

``` python
# 导入 omni.usd 模型
import omni.usd
```
此时，代码顶部应包含以下内容：
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

`omni.usd` 模块是核心 API 之一，通过它可以实现对 USD 和与 USD 相关的应用服务的访问。

### 第 6.3 步：找到 `_on_scatter()`
**向下滚动**，找到`_on_scatter()`，然后在 `transforms` 的变量声明代码前**添加**一行新代码。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/newline.png?raw=true)

`_on_scatter()` 会在用户按下扩展功能窗口中的`Scatter`按钮时调用。

### 第 6.4 步：获取 USD 上下文
 
在新添加的行下面，**声明** `usd_context`。请确保此行代码与 `if not prim_names:` 代码行齐头缩进。

``` python
usd_context = omni.usd.get_context()
```

完成添加后，您的代码应类似于如下示例：

``` python
def _on_scatter(self):
    """当用户按下“"Scatter"”（散布）按钮时调用"""
    prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
    if not prim_names:
        prim_names = get_selection()

    if not prim_names:
        # 待办事项：添加 “Can't clone”（无法复制）消息
        pass

    # 获取要锚定的 UsdContext
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
        target_path=self._scatter_prim_model.as_string，
        mode=self._scatter_type_model.get_current_item().as_string,
    )
```    
 
### 第 6.5 步：获取 Stage
在 `usd_context` 声明下，**添加** `stage = usd_context.get_stage()`。

``` python
# 存储要锚定的 UsdContext
usd_context = omni.usd.get_context()
# 从当前 UsdContext 获取 Stage
stage = usd_context.get_stage() 
```

变量stage将使用 USD 获取当前的 Stage。Stage 的层次结构中嵌着多个 prims。

### 第 6.6 步：从Stage获取源 Prim
在下一行中，**添加** `prim = stage.GetPrimAtPath(self._source_prim_model.as_string)`。
``` python
# 存储要锚定的 UsdContext
usd_context = omni.usd.get_context()
# 从当前 UsdContext 获取stage
stage = usd_context.get_stage() 
# 将当前扩展功能中被引用的 Prim保存起来
prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
```

### 第 6.7 步：获取源Prim的转换数据

接下来，我们需要添加 `position = prim.GetAttribute('xformOp:translate').Get()`，以**存储**prim的位置数据。检查了下面的示例代码后，请**保存** `window.py`。

``` python
# 存储要锚定的 UsdContext
usd_context = omni.usd.get_context()
# 从当前 UsdContext 获取stage
stage = usd_context.get_stage() 
# 存储扩展程序中当前引用的prim(基元)
prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
# 获取焦点基元的位置数据
position = prim.GetAttribute('xformOp:translate').Get() 
```

为了获得prim的位置，我们需要获取 Xform 中存储的转换值，从而得到选定的prim的 X 轴、Y 轴和 Z 轴坐标。

> **注意：**转换参数 (Xform) 是 Omniverse 中的所有对象的基本元素，决定了对象的位置。

检查您的代码，应该像下面的示例：

``` python
def _on_scatter(self):
    """当用户按下“"Scatter"”（散布）按钮时调用"""
    prim_names = [i.strip() for i in self._source_prim_model.as_string.split(",")]
    if not prim_names:
        prim_names = get_selection()

    if not prim_names:
        # 待办事项：添加 “Can't clone”（无法复制）消息
        pass

    # 存储要锚定的 UsdContext
    usd_context = omni.usd.get_context()
    # 从当前 UsdContext 获取stage
    stage = usd_context.get_stage() 
    # 保存扩展功能当前所引用的prim
    prim = stage.GetPrimAtPath(self._source_prim_model.as_string)
    # 获取聚焦的prim的位置数据
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
        target_path=self._scatter_prim_model.as_string，
        mode=self._scatter_type_model.get_current_item().as_string,
    )
```
 

 
## 第 7 步：使用选定的 Prim（基元）的位置作为散布原点

更新散布功能后，我们就可以传递前面计算的源prim的位置值了。
 
### 第 7.1 步：打开 window.py
**打开** `window.py`，在 `_on_scatter()` 中找到声明 `transforms` 的位置。

``` python
transforms = scatter(
    count=[m.as_int for m in self._scatter_count_models],
    distance=[m.as_float for m in self._scatter_distance_models],
    randomization=[m.as_float for m in self._scatter_random_models],
    id_count=len(prim_names),
    seed=self._scatter_seed_model.as_int
)
```
 
### 第 7.2 步：将位置值传递到 `scatter()`
在 `seed=self._scatter_seed_model.as_int` 后面，将代码 `source_prim_location=Gf.Vec3d(0,0,-500)` **替换为** `source_prim_location=position`。


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

### 第 7.3 步：进行测试
保存 `window.py` 并返回到 Omniverse。在stage中对某个prim执行**散布**操作。然后，再对另一个prim执行**散布**操作。注意观察它们如何仅在相应prim的位置处进行散布。

### 第 7.4 步：点击 `Play`（播放）
运行您的stage！

## 第 8.1 步（自我挑战）：为散布扩展功能添加随机化功能
现在，按下`Scatter`（散布）按钮后，对象会均匀地散布到stage中。请尝试更改代码，以实现随机分布。如果您找不到思路，请展开*提示*部分。

> **提示：**使用 `random.random()`。

<details>
<summary>提示</summary>

### 第 8.1.1 步（自我挑战）：打开 `scatter.py`

**打开** `scatter.py`，并*找到* `scatter()`。

 
### 第 8.1.2 步（自我挑战）：添加随机值
**找到**用于生成 Vec3d 的 `result.SetTranslate()` 代码。将传递的第一个参数**修改**为 `source_prim_location[0] + (x + random.random() * randomization[0]),`。

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + (x + random.random() * randomization[0]),
        source_prim_location[1] + y,
        source_prim_location[2] + z,
    )
)
```

`randomization[0]` 指的是 Scatter 扩展功能窗口中标记为 Random 的选项。

### 第 8.1.3 步（自我挑战）：同样修改 Y 值和 Z 值
按照上一步中的操作，对传递到 *Vec3d* 构造的 Y 值和 Z 值进行相同的**修改**。

``` python
result.SetTranslate(
    Gf.Vec3d(
        source_prim_location[0] + (x + random.random() * randomization[0]),
        source_prim_location[1] + (y + random.random() * randomization[1]),
        source_prim_location[2] + (z + random.random() * randomization[2]),
    )
)
```

### 第 8.1.4 步（自我挑战）：更改随机值
**保存** `scatter.py`，然后**返回到** Omniverse。**修改**“*Scatter Window*”（散布窗口）中的“*Random*”（随机）参数。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/random.png?raw=true)

### 第 8.1.5 步（自我挑战）：对多个基元执行散布操作
**单击**`Scatter`（散布）按钮，并查看基元的散布情况。

> **注意：**如果散布范围很小，请增大“Random”（随机）值。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/randomscatter.png?raw=true)

 
</details>


# 第 III 部分 散布物体

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-02-v1-zh/3DLayoutToolsWorkshop3_CN_v1.mp4" type="video/mp4">
</video>
 
 
## 第 9 步：对一个大理石 Prim（基元） 执行散布操作

Stage 中包含多个大理石 prims（基元），可用于四处散布。
 
### 第 9.1 步：在 *Stage* 中选择一个大理石基元 
转到 `Stage` 部分，**展开** “Marbles”（大理石），然后**选择**任意大理石基元。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleselect.png?raw=true)
 
### 第 9.2 步：将所选大理石的路径复制到散布扩展功能
选择好大理石素材后，**单击** `Scatter Window` （散布窗口）中的 `S` 按钮。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)

### 第 9.3 步：更改 X 轴的距离值
将`X Axis`（X 轴）的 `Distance`（距离）值**更改**为 10

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/distance10.png?raw=true)

### 第 9.4 步：单击`Scatter`（散布）按钮
**单击**窗口底部的 `Scatter`（散布）按钮。
> **注意**：如果看不到 `Scatter`（散布）按钮，请在 `Extentions` 窗口中向下滚动，或者拉动右下角**扩大** `Extentions`窗口。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)

单击 `Scatter`（散布）按钮后，您的 stage 应该与下面的示例类似。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/marbleScattered.png?raw=true)
 
## 第 10 步：观看 Stage 里的动画

`Play`（播放）按钮的作用不仅是播放动画或影片，我们也可以用它进行物理学仿真。
 
### 第 10.1 步：单击 `Play`（播放）按钮
对大理石基元设置了散布功能后，我们可以观看散布的动画效果。**单击** `Play`（播放）按钮观看 stage。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbutton.png?raw=true)
 
按下 `Play`（播放）按钮后的效果：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbuttonaction.gif?raw=true)

> **注意**：要**重置** stage，请**单击** `Stop`（停止）按钮。

### 第 10.2 步：选择其他的 Prims（基元）
在 `Stage` 选项下，**选择**另一个 prim（基元）。您可以选择另一个大理石 prim（基元），也可以选择瓶、碗或其他 prim（基元）。

我们建议使用下面圈出的任意 prim：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/primstoselect.png?raw=true)

### 第 10.3 步：将选定的 Prim 复制到散布窗口
选好 prim 后，**单击** `S` 按钮，将 prim 的路径复制到 `Scatter` 窗口里。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/clickS.png?raw=true)
 
### 第 10.4 步：更改散布参数
**更改** `Scatter Window`（散布窗口）中的某些参数。例如：在 `Y Axis`（Y 轴）部分，分别将 `Object Count`（对象数量）和 `Distance` （距离）的值**更改**为 20 和 5。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/params.png?raw=true)

### 第 10.5 步：对新 Prim（基元）执行散布操作
**单击** `Scatter Window`（散布窗口）底部的 `Scatter`（散布）按钮。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterbutton.png?raw=true)
 
### 第 10.6 步：单击 `Play`（播放）按钮
**单击** `Play`（播放）按钮，并观看Stage的动画效果。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/playbutton.png?raw=true)

尝试使用散布扩展功能在 stage 中散布多种物品，并进行播放。

## 第 11 步（自我挑战）：按照给定的缩放倍数对散布的 Prim 进行缩放

您可能注意到，窗口中有一个 `Scale`（缩放）选项。但是，这个选项未发挥任何作用。我们来试着让它派上用场。如果您找不到思路，请展开*提示*部分。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scale.png?raw=true)

> **提醒：**可以查看 `window.py`，看看这个值是在哪里使用的。

<details>
<summary>提示</summary>

### 第 11.1 步（自我挑战）：在 `window.py` 中，找到 `duplicate_prims()`
在 `window.py` 中，**找到** `duplicate_prims()`。

``` python
duplicate_prims(
    transforms=transforms,
    prim_names=prim_names,
    target_path=self._scatter_prim_model.as_string，
    mode=self._scatter_type_model.get_current_item().as_string
)
```
`duplicate_prims()` 会接收所有转换参数，并根据选定的模式复制选定的基元。它非常适合添加到 scale 参数中。

### 第 11.2 步（自我挑战）：在 `duplicate_prims()` 中传递范围值
`self._scale_models` 储存了“*Scatter Window*”（散布窗口）中的每一项范围设置。在 `duplicate_prims()` 中，**添加** `scale=[self._scale_models[0].as_float, self._scale_models[1].as_float, self._scale_models[2].as_float]`。

``` python
duplicate_prims(
    transforms=transforms,
    prim_names=prim_names,
    target_path=self._scatter_prim_model.as_string，
    mode=self._scatter_type_model.get_current_item().as_string,
    scale=[self._scale_models[0].as_float, self._scale_models[1].as_float, self._scale_models[2].as_float]
)
```

### 第 11.3 步（自我挑战）：在 `utils.py` 中，找到 `duplicate_prims()`
从 `ext/omni.example.scene_auth_scatter > omni/example/ui_scatter_tool > utils.py` **打开** `utils.py`。**找到** `duplicate_prims()`。

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy"):
```

### 第 11.4 步（自我挑战）：向 `duplicate_prims()` 添加新参数
向 `duplicate_prims()` **添加**新参数 `scale: List[float] = [1,1,1]`。

``` python
def duplicate_prims(transforms: List = [], prim_names: List[str] = [], target_path: str = "", mode: str = "Copy", scale: List[float] = [1,1,1]):
```

### 第 11.5 步（自我挑战）：将缩放倍数参数传递到 Kit Command
**向下滚动**，找到 `omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform)`。
将 `new_scale=scale` **添加**到 Kit Command。

``` python
omni.kit.commands.execute("TransformPrimSRT", path=path_to, new_translation=new_transform, new_scale=scale)
```
 
### 第 11.6 步（自我挑战）：保存并测试
**保存**文件，然后尝试使用不同的缩放值对基元执行散布操作。

![](images/scatterscale.gif)
![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_1/exts/omni.example.scene_auth_scatter/workshop/images/scatterscale.gif?raw=true)
 
</details>

## 恭喜！
您已完成本培训！希望您在学习和使用 Omniverse 的过程中找到乐趣！

[欢迎在 Discord 上加入我们，进行更深入的交流！](https://discord.com/invite/nvidiaomniverse)
