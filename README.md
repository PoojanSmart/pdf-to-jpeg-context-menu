# Context menu for converting pdf to jpeg

Opens context menu when user right clicks on .pdf file to convert it to .jpeg.

## Requirements

1. Python, dependencies: pdf2image, tqdm  

## Configure

1.  create a directory in C:/
2.  Put the python script and zip to the directory.
3.  Unzip the zip file.
4.  Open registry editor.
5.  Take back up of current registry.
6.  Go to `Computer\HKEY_CLASSES_ROOT\SystemFileAssociations\` path in registry.
7.  Create key hierarchy as following .pdf -> shell -> shell -> Conver to jpg [Context button name] -> command.
8.  In last key (command), add following command  : `[python path] C:\Tools\pdf-to-jpg.py "%1"` 

## Preview

![Context menu appears with option to convert to jpeg for pdf file](https://github.com/PoojanSmart/pdf-to-jpeg-context-menu/assets/44301271/5168797c-45ec-479f-85d7-b1ebfbae1df0)

![Result](https://github.com/PoojanSmart/pdf-to-jpeg-context-menu/assets/44301271/94587ade-7f65-4a5f-af8d-a03345902b4d)



