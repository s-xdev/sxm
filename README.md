## **SXM** (a stupid project thingy i made in my free time)

### Why: 
🐈

## How to use this

Basically you put the python file (or exe if i build it) into your desktop/whatever directory you use to store your projects.

There are 2 commands that are kind of irrelevant, ***exit***, and ***clear***.

Other than that, the main command is open. The reason the files has to be inside of the desktop or inside a directory where you keep projects, is that when you run the open command it will look like this:

```
cwdwhateveritis$:> open projectContainerFolder:ProjectFolder
```

Or, for me it would be like this:

```
cwdwhateveritis$:> open github:sxm
```

Also **It might give certain errors such as when a directory you inputted does not exist, it will throw an error saying the directory is invalid.**

One other thing, is if there is not a `sxm.config.json` file present in the folder, it will not work because it requires a startup command.

Because of the fact I use vscode, I use the built-in `code` command it ships with, so my `sxm.config.json` file looks like:

```json
{
    "StartupCommand": "code {dir_location}"
}
```

The reason it has the **{dir_location}** inside of it is so when ran it will open code inside of the directory where it is stored, and the code already cleans it up by replacing **{dir_location}** with the directory of the project. You can edit the startup command to make it work with your editor, but other than that  this is basically it.

**Note: It replaces every "{dir_location}" with the project file directory, so keep that in mind for commands.**