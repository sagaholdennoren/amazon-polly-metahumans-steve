# Amazon Polly & MetaHumans Sample Project

## NOTES:<br>
-- You have to have an active AWS account<br>
-- This works for Unreal Engine 4.27 "only"<br>
-- Install Visual Studio 2019 for C++/Games development<br>
-- If using google speech to text then an active google api account<br>
-- Install cmake 3.18.0.rc1 <br>
-- Install "dotNet" component located here ----> https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-6.0.408-windows-x64-installer<br>
-- Change your "Config/DefaultEditorSettings.ini" to use Visual Studio 2019 like so<br>
-----  [/Script/SourceCodeAccess.SourceCodeAccessSettings]<br>
-----  PreferredAccessor=VisualStudio<br>
-- Run batch file located at ----> Source/AmazonPollyMetaHuman/ThirdParty/AwsSdk/BuildAwsSdkWin64.bat<br>
-- Right click Unreal project and select "Build VS project files"<br>
-- Once VS "solution file -- *.sln" apears, load VS solution and select main menu ->Build->Rebuild Solution<br>
-- Wait till done building<br>
-- Load aws polly project<br>
<br>


*A sample project combining Epic Games' MetaHuman digital characters with Amazon Polly text-to-speech.*

This Unreal Engine sample project demonstrates how to bring Epic Games' [MetaHuman digital characters](https://www.unrealengine.com/en-US/digital-humans) to life using the Amazon Polly text-to-speech service from AWS. Use this project as a starting point for creating your own Unreal Engine applications that leverage Amazon Polly to give voice to your MetaHumans using one of 16 different English language voices spanning 5 dialects. Or extend this project to use any of Polly's 60+ voices covering 20+ languages and 13+ dialects.


https://user-images.githubusercontent.com/52681180/144937529-6b967a38-6b25-44ee-b419-b7bd4c1fa42c.mov


With Amazon Polly, you only pay for what you use. You are charged based on the number of characters of text that you convert either to speech audio or to speech metadata. In addition, you can cache and replay Amazon Polly’s generated speech at no additional cost. For full pricing details, see [Amazon Polly Pricing](https://aws.amazon.com/polly/pricing/).

**Contents**

- [Quick Start](#quick-start)
- [Developer Guide](#developer-guide)
- [Getting Help](#getting-help)
- [Security](#security)
- [License](#license)




## Quick Start



> 🛑 Before proceeding you must have Unreal Engine 4.26 or 4.27 installed as well as the Microsoft Visual Studio development tools required for UE4 C++ development (Windows) or the Xcode development tools (Mac). If you need help with these setup steps, refer to the Unreal Engine 4 documentation, especially ["Setting Up Visual Studio for Unreal Engine"](https://docs.unrealengine.com/4.26/en-US/ProductionPipelines/DevelopmentSetup/VisualStudioSetup/). Disclaimer: This was only tested with Visual Studio 2019 with UE4.26, although with slight modifications to the build script it should work with Visual Studio 2022 as well. I couldn't get this to work with UE5.



### 1. Create AWS credentials for the project

In order for this Unreal Engine project to interact with the Amazon Polly service, you must provide it with AWS credentials that allow access to that service. The easiest way to generate these credentials is to create a new AWS Identity Access & Management (IAM) user in your AWS account. 

Create a new IAM user and assign to it the permissions policy named *"AmazonPollyReadOnlyAccess"*. Although the name you give this user is not important, we suggest naming it "MetaHumans Sample" or something equally distinctive. Be sure to save the **Access Key ID** and the **Secret Access Key** that are generated during the user creation process. You'll need them later.

> 💡 **Tip:** For more help, see ["Creating an IAM user in your AWS account"](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in the AWS IAM documentation.



### 2. Install and configure the AWS Command Line Interface

You will need to configure your local computer to communicate with AWS services using the credentials you created above. The easiest way to do this is to install and configure the AWS Command Line Interface (AWS CLI).

Install the AWS CLI to your local computer following [these instructions](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).

Use the `aws configure` command to create a default profile for the AWS CLI. Be sure to use the **Access Key ID** and **Secret Access Key** values you saved above.

> 💡 **Tip:** For more help, see ["Configuration basics"](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) in the AWS CLI documentation.



### 3. Compile the Polly C++ SDK

> 🛑 This next step requires cmake and git. If you don't already have cmake installed, you can [download it here](https://cmake.org/download/). After you download cmake, launch cmake and click 'Tools' -> 'How To Install For Command Line Use' and follow one of the instructions. E.g. for Mac - One may add CMake to the PATH: PATH="/Applications/CMake.app/Contents/bin":"$PATH"

This project makes use of the C++ Polly API – a part of the AWS SDK for C++ – to communicate with the Polly service. We've provided scripts to automatically download and compile the appropriate binaries for you. Run one of the following scripts:

**Windows:** [Source/AmazonPollyMetaHuman/ThirdParty/AwsSdk/BuildAwsSdkWin64.bat](Source/AmazonPollyMetaHuman/ThirdParty/AwsSdk/BuildAwsSdkWin64.bat)

**Mac:** [Source/AmazonPollyMetaHuman/ThirdParty/AwsSdk/BuildAwsSdkMac.sh](Source/AmazonPollyMetaHuman/ThirdParty/AwsSdk/BuildAwsSdkMac.sh)



### 4. Open the Unreal Engine project

Open the project by double-clicking on the *AmazonPollyMetaHuman.uproject* file.

Click "Yes" on the dialog that appears.

<img src="Documentation/media/module-compile-prompt.png" alt="Module compile prompt" style="width: 33em;" />



### 5. Run the project

To try out the project, simply click the "Play" button in the Unreal Engine editor. The MetaHuman will come alive using speech and lip sync generated by Amazon Polly. After the MetaHuman stops speaking you can enter your own custom speech text into the on-screen text field.

![Play button](Documentation/media/UE4-toolbar-play.png)



> ⚠️ Wait until the "Compiling Shaders" process completes before running this project for the first time.
>
> <img src="Documentation/media/compiling-shaders.png" alt="&quot;Compiling Shaders&quot; message" style="width: 30em;" />



> 🛠 **Troubleshooting:** This project includes extensive error messaging that can help you debug common problems.  If the project doesn't work properly, open the Output Log tab in the Unreal Engine editor and look for error messages.



## Developer Guide

This repository includes a full [Developer Guide](Documentation/DeveloperGuide.md) which describes the project's architecture and explains how to customize the project with your own MetaHuman characters.



## Getting Help

If you have questions as you explore this sample project post them to the [Issues](./issues) section of this repository. To report bugs, request new features, or contribute to this open source project see [CONTRIBUTING.md](CONTRIBUTING.md).



## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.



## License

This sample code is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.

