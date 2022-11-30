

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/logo.png?raw=true)

# NVIDIA OMNIVERSE

# 通过 NVIDIA Omniverse 构建自定义 3D 场景操作工具

了解如何在易于扩展的模块化的 Omniverse 平台上构建高级工具。Omniverse 开发者团队将向您展示如何扩展并增强您所熟悉且喜爱的 3D 工具。

# 学习目标
- 启用扩展程序
- 将 `scale` 函数附加至滑块小组件上

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-06-v1-zh/sceneManipulatorIntro_CN_v1.mp4" type="video/mp4">
</video>
 
# UI Scene_Widget Info

## 第 I 部分

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-06-v1-zh/sceneManipulator1_CN_v1.mp4" type="video/mp4">
</video>
 
### 第 1 步：打开 Workshop 场景

#### <b>第 1.1 步：从下面提供的链接下载 Stage</b>

[Stage 下载链接](https://dli-lms.s3.amazonaws.com/assets/x-ov-05-v1/Stage.zip)

#### <b>第 1.2 步：使用“Extract All...”（提取所有文件...）选项解压 Stage 文件

此操作会创建一个名为 `Stage` 的解压文件夹。

#### <b>第 1.3 步：在 Omniverse 中打开 Stage

在 Omniverse Code 的 `Content` 选项卡，找到系统中存放 Stage 文件的位置。
  
（即 C:/Users/yourName/Downloads/Stage）
 
在 Omniverse Code 控制台底部的 `Content` 选项卡中，**双击**中间窗格中的 `Stage.usd` 即可在视图（Viewport）中打开该 Stage。

### 第 2 步：安装小组件扩展功能

#### <b>第 2.1 步：打开`Extensions`（扩展功能）选项卡</b>

单击 `Extensions`（扩展功能）管理器选项卡。

#### <b>第 2.2 步：对社区/第三方的扩展功能进行筛选</b>

选择 `Community/Third Party`（社区/第三方）选项卡
<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/extensionCommunity.PNG?raw=true)

<br>

#### <b>第 2.3 步：搜索小组件信息</b>

搜索 `Widget Info` 并单击 `Omni UI Scene Object Info With Widget Example`

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/widgetExt.png?raw=true)

#### <b>第 2.4 步：安装/启用扩展程序</b>

单击选中的扩展程序，然后在右侧控制台中单击 `Install`（安装）。安装后，启用扩展程序。

><span>❗</span>您可能会收到一个警告，指明此扩展程序未经验证。您可以安全地安装此扩展程序。

<br>

#### <b>第 2.5 步：检查小组件是否起作用</b>

前往 `Viewport`（视图），然后在层次结构中选择一个 `prim`（基元）。

`prim` 是“primitive”（基元）的缩写。基元是 Omniverse 中的基本单元。在 `USD`(Universal Scene Description) 场景中导入或创建的任何对象都是一个基元。这包括：镜头、声音、光线、网格等等。

您会在视图中的 `prim` 上方看到以下小组件：

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/viewportWidgetEnabled.PNG?raw=true)

<br>

><span>❓</span> 您注意到了吗？
>- 基元的路径显示在小组件中。
>- 小组件中有一个缩放滑块，但它不起作用！我们将在下一部分中修复此问题。

<br>

#### <b>第 3 步：找到播放按钮</b>

在视口中找到 `Play`（按钮），并看看单击它时会发生什么！别忘了在完成后按 `Stop`（停止）按钮。

<details>
<summary>单击此处可查看按钮所在的位置</summary>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/playButton.png?raw=true)

</details>

<br>

>#### <span>🧠</span><b>第 4 步（自我挑战）：头脑风暴用例</b>
><i>本培训中的所有挑战都是可选的。</i>
>
>思考小组件的 3 种使用方式。例如，您注意到它可用来显示 prim 的路径，那么您还可以在小组件中显示 prim 的其它信息吗？与同行进行头脑风暴，并思考如何将小组件应用于您所从事的行业！稍后我们将就此进行小组讨论。

<br>

<br>

>### <span>⛔</span>建议在此处停留，思考一下，再继续学习第 II 部分

<br>

## 第 II 部分

<video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-06-v1-zh/sceneManipulator2Intro_CN_v1.mp4" type="video/mp4">
 </video>

 <video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-06-v1-zh/sceneManipulator2_CN_v1.mp4" type="video/mp4">
 </video>
  
### 第 5 步：找到您的工作文件

#### <b>第 5.1 步：打开 Visual Studio</b>

转至 `Extensions`（扩展功能）选项卡。

单击 `Widget Info`（小组件信息）扩展功能以在右侧打开扩展功能概述。

单击文件夹图标旁边的 `VS Code` 图标：

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/vsCodeIcon.PNG?raw=true)

<br>

系统将弹出单独的 `VS Code` 窗口，如下所示：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/vsCodeopened.png?raw=true)

<br>


#### <b>第 5.2 步：找到操控器脚本</b>

在左列下拉菜单中的以下位置找到此会话所需的文件：

 `exts -> omni.example.ui_scene.widget_info\omni\example\ui_scene\widget_info`

您当前位于：

`widget_info_manipulator.py`

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/fileStructLocation.gif?raw=true)

<br>

### 第 6 步：修复损坏的滑块
>#### 第 6.1 步：添加新导入

在脚本顶部找到 `imports`。

添加新导入：

```python
from pxr import Gf
```

现在，导入的库将如下所示：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/newImport.png?raw=true)

<br>

在以下步骤中，您将使用 `Graphics Foundation`（简称 Gf），它是一个包含基础图形类和操作的软件包。

#### <b>第 6.2 步：找到函数 `update_scale`</b>

在脚本底部找到以下函数：

```python
         # 更新滑块
        def update_scale(prim_name, value):
```

此函数会更新小组件中的滑块。但是，它目前没有任何代码用来更新缩放比例。让我们开始添加所需的代码来实现这一点！

#### <b>第 6.3 步：获取当前场景</b>


在 `update_scale` 函数内部，找到 `print` 调用。

定义`stage` 变量，例如：

```python
            stage = self.model.usd_context.get_stage()
```

从 USD 上下文中，我们抓取当前活动的stage，并将其存储到 `stage` 变量中。

`Stage` 是您的 prims 在层次结构中嵌套的地方。


现在，`update_scale` 应如下所示：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/GetStage.png?raw=true)

<br>

><span>❗</span>请确保新的 stage 变量与 print 调用的缩进列是对齐的。否则，请添加或删除制表符（tab键），直到实现对齐。

<br>

#### <b>第 6.4 步：获取已选择的 prim（基元）</b>

接下来，在stage 变量的下面为当前选择的 prim 添加变量：

```python
            prim = stage.GetPrimAtPath(self.model._current_path)
```

`update_scale` 现在如下所示：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/getPrim.png?raw=true)

><span>❗</span> 此 prim 变量应与其上方的 stage 和 print 调用保持对齐。

<br>

#### <b>第 6.5 步：更新 `scale`</b>

在下一行中添加新的 `scale` 变量。

在此变量中，您将获得`xform` 的 `scale`（缩放比例）属性，然后设置 `scale` 的 `Vector3` 值，如下所示：

```python
            scale = prim.GetAttribute("xformOp:scale")
            scale.Set(Gf.Vec3d(value, value, value))
```

现在，您已完成，`update_scale` 函数将如下所示：

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/setScale.png?raw=true)

><span>❗</span>`scale` 变量应与其上方的变量保持对齐。

<br>

### 第 7 步：它起作用了吗？

#### <b>第 7.1 步：保存并测试！</b>

保存操控器脚本，并检查缩放滑块在小组件中是否起作用！

><span>❗</span>  保存时，您可能会注意到小组件在视口中消失。这是预期行为，再次单击基元即可显示小组件。

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/scaleWorking.gif?raw=true)

函数 `update_scale` 正在更新您的滑块，在此函数中，您添加了可获取 `stage` 和当前所选择的 `prim`（小组件显示在其上方）的属性，然后在滑块移动时调用 scale 的 Vector3，以在各个方向上改变 prim（基元）的大小。

><span>❗</span>不起作用？ 查看 `Console`（控制台）以调试任何错误。
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/Console.png?raw=true)

<br>

>#### &#128161; <b>第 8 步（自我挑战）：更大的缩放比例</b>
><i>本培训中的所有挑战都是可选的。</i>
>
>您能否更改函数，实现对一个 prim（基元）以大于 1.0 的比例进行缩放？
>
><details>
><summary>单击此处获取答案</summary>
>
>设置 `value` 变量，并将其值乘以一个数字。
>
>例如：
>
>```python
>        def update_scale(prim_name, value):
>            if value <= 0:
>                value = 0.01
>            print(f"changing scale of {prim_name}, {value}")
>            ## 新的值变量添加在下方
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

>#### <span>&#129504;</span><b>第 9 步（自我挑战）：您希望使用小组件控制其他哪些属性？</b>
><i>本培训中的所有挑战都是可选的。</i>
>
> 针对您可能要添加到此小组件的其他 3-5 个属性展开头脑风暴。稍后我们将就此进行公开讨论。

<br>

>### <span>⛔</span> 建议在此处停留，思考一下，再继续学习第 III 部分。

<br>

## 第 III 部分：
 
 <video width="560" height="315" controls>
<source src="https://dli-lms.s3.amazonaws.com/assets/x-ov-06-v1-zh/sceneManipulator3_CN_v1.mp4" type="video/mp4">
 </video>
  
### 第 10 步：创建您的场景

#### <b>第 10.1 步：缩放各种物品！</b>

在您的场景中随意选取一个 prim（基元）并缩放它，例如变出非常大的大理石或很小的罐子。

如何打造独特的场景？

><span>&#11088;</span>请在完成后按 `Play`（播放）按钮！
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/playButton.png?raw=true)

<br>

![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/section3.gif?raw=true)

<br>

>#### <span>&#129504;</span><b>第 11 步（自我挑战）：在一个轴上缩放</b>
><i>本培训中的所有挑战都是可选的。</i>
>
>您能否更改函数，实现仅在一个坐标轴的方向上对基元进行缩放？
>
><details>
><summary>单击此处获取答案</summary>
>
>对于您不希望进行缩放的轴方向，在 `scale.Set(Gf.Vec3d(value,value,value))` 中将对应该坐标轴的值更改为 1。
>
>例如：
>
>```python
>scale.Set(Gf.Vec3d(value,1,1))
>```
>
>这会将缩放更改为仅在 X 轴上进行，因为 Y 轴和 Z 轴的值保留为 1，而 X 轴会更改。
>
></details>

<br>

>#### <span>&#129504;</span><b>第 12 步（自我挑战）：打开光线操控器</b>
><i>本培训中的所有挑战都是可选的。</i>
>
>打开光线操控器扩展程序，然后单击面光源。
>
>如何使用此工具更改光线强度？
>
><details>
><summary>单击此处获取答案</summary>
>
>在 `Extensions`（扩展功能）选项卡中，在 `Community/Third Party`（社区/第三方）中搜索“Light”（光线），然后安装/启用 `Omni.Ui Scene Sample for Manipulating Select Light` 扩展程序。
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/LightExt.png?raw=true)
>
><br>
>
>在层次结构中选择一个面光源。
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/RectLight.png?raw=true)
>
><br>
>
>使用光标抓取光线工具的边，然后通过向前或向后拖动来更改光线强度。
>
>![](https://github.com/NVIDIA-Omniverse/kit-workshop-siggraph2022/blob/workshop_2/exts/omni.example.ui_scene.widget_info/Workshop/images/RectIntensity.png?raw=true)
>
></details>

<br>


## 恭喜！
您已完成本培训！希望您喜欢学习和使用 Omniverse！ 

[欢迎在 Discord 上加入我们，进行更深入的交流！](https://discord.com/invite/nvidiaomniverse)
