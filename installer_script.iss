; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "File Scanner"
#define MyAppVersion "1.0"
#define MyAppPublisher "Your Company Name"
#define MyAppExeName "file_scanner.exe"

[Setup]
AppId={{754b2181-ff5c-4610-935d-1274df257883}} 
AppName={#File_Scanner}
AppVersion={#1.0}
AppPublisher={#MihaiS}
DefaultDirName={autopf}\{#MyAppName}  ; Installs to C:\Program Files\File Scanner
DefaultGroupName={#MyAppName}
OutputDir=.\dist
OutputBaseFilename=FileScannerSetup
Compression=lzma
SolidCompression=yes
; SetupIconFile=.\path\to\your\icon.ico  ; Optional: Uncomment and specify an icon file

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: ".\dist\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
; Add more files here if needed, e.g., Source: ".\path\to\file"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{group}\{cm:UninstallProgram,{#MyAppName}}"; Filename: "{uninstallexe}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#MyAppName}}"; Flags: nowait postinstall skipifsilent
