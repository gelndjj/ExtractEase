<a name="readme-top"></a>

[![Contributors][contributors-shield]](https://github.com/gelndjj/ZIP_File_Extractor/graphs/contributors)
[![Forks][forks-shield]](https://github.com/gelndjj/ZIP_File_Extractor/forks)
[![Stargazers][stars-shield]](https://github.com/gelndjj/ZIP_File_Extractor/stargazers)
[![Issues][issues-shield]](https://github.com/gelndjj/ZIP_File_Extractor/issues)
[![MIT License][license-shield]](https://github.com/gelndjj/ZIP_File_Extractor/blob/main/LICENSE)
[![LinkedIn][linkedin-shield]](https://www.linkedin.com/in/jonathanduthil/)


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/gelndjj/ZIP_File_Extractor">
    <img src="https://github.com/gelndjj/ZIP_File_Extractor/blob/main/resources/image0.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">ZIP File Extractor</h3>

  <p align="center">
    Archive Management Tool
    <br />
    <a href="https://github.com/gelndjj/ZIP_File_Extractor"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/gelndjj/ZIP_File_Extractor/issues">Report Bug</a>
    ·
    <a href="https://github.com/gelndjj/ZIP_File_Extractor/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project
<div align="center">
<img src="https://github.com/gelndjj/ZIP_File_Extractor/blob/main/resources/image0.png" alt="Logo" width="128" height="128">
</br>
This ZIP File Extractor is a powerful, easy-to-use Python application built with tkinter, designed to streamline the process of extracting ZIP, 7z, and RAR files. It allows users to select directories, view file structures, and extract compressed files with ease, offering both specific and bulk extraction functionalities.</br> 
</br>
<img src="https://github.com/gelndjj/ZIP_File_Extractor/blob/main/resources/app_osx.png" alt="Screenshot" width="762" height="490">
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

# Usage 

Launch the application.
Navigate through the file system tree to find and select the directory containing the compressed files.
Choose the type of extraction - specific extension or raw extraction.
Monitor progress through the integrated progress bar.
View logs and results in the GUI.

# Usage Documentation

### Launching the Application

+ Open the Application: Start the application to view the main window, which displays the file system tree and various extraction options.
Navigating and Selecting Files

+ File System Tree: Use the tree view to navigate through the file system. Select a folder to view its contents and choose files for extraction.

### Extraction Options

+ Extract Specific Extension (Same Folder): Click this button to extract files with a specific extension from the selected directory. The files are extracted to the same folder.
+ Extract Specific Extension (Specific Folder): This button allows you to extract files with a specific extension from the selected directory into a different, user-specified folder.
+ RAW Extraction (Same Folder): Use this button for a bulk extraction of all supported archive files (ZIP, 7z, RAR) in the selected folder. The extracted files are saved in the same directory.
+ RAW Extraction (Specific Folder): Similar to the above, but allows you to choose a different destination folder for the extracted files.
Monitoring Progress

- - Progress Bar: The progress bar at the bottom of the application provides real-time feedback on the extraction process, showing how much work has been completed.

### Error and Success Reporting

+ Error and Success Logs: After the extraction process, a new window displays the successful extractions and any errors encountered, providing detailed information about each processed file.

### Additional Features
+ File System Refresh: The file system tree is dynamically updated to reflect changes in the directory structure.
+ Multi-Threaded Extraction: The application uses threading to ensure that the UI remains responsive during the extraction process.


<!-- GETTING STARTED -->
## Standalone APP

Install pyintaller
```
pip install pyinstaller
```
Generate the standalone app
```
pyinstaller --onefile your_script_name.py
```

## Create DMG(MacOS)

#### Step 1: Create a New Folder for DMG Contents

##### 1. Create a New Folder:
+ Create a new folder on your desktop or in another convenient location. 
+ This folder will hold the contents of your * . dmg file.
+ Name it something like 'DMGContents" or similar.

##### 2. Copy Your App and Applications Shortcut:
+ Copy your "YourApp.app* file into this new folder.
+ Open a new Finder window and go to the /Applications' folder.
+ Drag the Applications folder into your 'DMGContents" folder while holding down the Cmd and 'Alt keys. This will create an alias (shortcut) to the Applications folder in your 'DMContents" folder.

#### Step 2: Create the DMG File
+ Now, use Disk Utility or the 'hdiutil command to create your . dm file from the "DMGContents" folder.
+ Using Disk Utility:

Follow the steps previously described but select the DMGContents* folder instead of just the app.
+ Using Terminal with hdiutil:
+ Use the hdiutil' command like before, but point it to your DMContents" folder.

For example:
```
hdiutil create -volname "YourApp" -srcfolder /path/to/YourApp.app -ov -format UDZO YourApp.dmg
```

#### Step 3: Customize the DMG Appearance (Optional)
+ To make the . dmg file look more professional, you can customize its appearance:

+ Mount the DMG: Double-click the " . dmg" file to mount it.
+ Open the Mounted Volume: Open the mounted volume in Finder.
+ Arrange Icons: Arrange the app and the Applications shortcut in a way that encourages the user to drag the app into the Applications folder.
+ You can add text instructions or use a background image to make this more intuitive.
+ Set Icon Sizes and View Options:

Set the icon size and the view options as you prefer (e.g., using 'View Show View Options' in Finder).

+ You can make these view options default for all who open the dm by clicking
+ Use as Defaults" at the bottom of the view options window.
+ Eject and Test:
+ After arranging everything, eject the dm (by dragging the mounted volume to the Trash or right-clicking and selecting 'Eject *) and then remount it to ensure your changes are saved.

#### Step 4: Distribute the DMG File
Once you're satisfied with the appearance and functionality, your * . dm file is ready for distribution.

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Built With

<a href="https://www.python.org">
<img src="https://github.com/gelndjj/ZIP_File_Extractor/blob/main/resources/py_icon.png" alt="Icon" width="32" height="32">
</a>
<p align="right">(<a href="#readme-top">back to top</a>)</p>
    

<!-- LICENSE -->
## License

Distributed under the GNU GENERAL PUBLIC LICENSE. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact


[LinkedIn](https://www.linkedin.com/in/jonathanduthil/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
