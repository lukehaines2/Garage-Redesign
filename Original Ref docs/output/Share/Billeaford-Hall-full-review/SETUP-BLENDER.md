# Agent workflow: install Blender if needed and open the review

This workflow starts when Dad asks Agent to run/setup/open the pack using the starter prompt. Its purpose is to open the existing review assets, not regenerate them.

## 1. Find the pack and the computer type

Locate the directory containing this file, `AGENTS.md` and `START-HERE.html`. Confirm `output/V4/model/garage-V4-review.blend` exists. Use this actual location for every path; the folder may be renamed or under Downloads with spaces in its name. Work with a fully extracted directory, not an operating system's ZIP preview.

Detect Windows/macOS/Linux and CPU architecture. Use the agent's local terminal and application tools. Prefer the already-installed Blender if version 4.5 or newer can open this file. The supplied model was saved with **Blender 4.5.10 LTS**; Blender **4.5 LTS** is the reproducible default if a new installation is needed. Do not downgrade, uninstall or replace another working Blender installation unnecessarily.

## 2. Check for Blender; install it if absent or unsuitable

- **macOS:** check PATH, `/Applications/Blender.app` and the user's `Applications` folder. Read the executable's version. If needed, use Blender's official download site to obtain the correct Apple Silicon or Intel 4.5 LTS DMG. Mount it and copy `Blender.app` to an appropriate Applications folder; a user-owned Applications folder can avoid system-wide installation. Retain any existing differently versioned app. Launch the installed app, rather than relying on a temporary mounted download.
- **Windows:** check PATH and the installed Blender Foundation folders in Program Files or a known user installation. Read `blender.exe --version`. If needed, download the matching official Windows package. A portable ZIP extracted into a user-owned application folder is suitable and normally avoids administrator installation; the official installer is also an option. Discover the actual executable location afterwards. Do not assume the installation has added Blender to PATH.
- **Linux:** check PATH and any existing user-owned Blender install. If needed, download the matching official Linux release archive and extract it into a user-owned application folder. A suitable existing distribution package can be reused. A desktop/graphics session is needed to display the GUI; a remote/headless terminal alone does not show a window on Dad's desktop.

Use [Blender's official downloads](https://www.blender.org/download/) or the [official 4.5 release archive](https://download.blender.org/release/Blender4.5/). Confirm the selected release supports the machine, use the correct architecture, and verify the official checksum/signature when available. Do not invent a download URL or use an unofficial repack. Do not build Blender from source or install unrelated developer tools just to view this pack.

Use normal permission prompts for the requested install. If an administrator password, first-launch approval or manual installer step is required, explain that exact step for Dad. Do not disable OS protections, remove quarantine flags to bypass a warning, suppress required consent, or turn this into an unattended security workaround.

The platform guidance above follows the [official macOS installation guide](https://docs.blender.org/manual/en/4.4/getting_started/installing/macos.html) and [official Windows installation guide](https://docs.blender.org/manual/id/4.4/getting_started/installing/windows.html); use the current official instructions for the release actually selected. No specific installer is bundled in this review ZIP.

## 3. Open the existing model and review page

Check the executable version, then open the **GUI**, not Blender's background mode, with the full path to `output/V4/model/garage-V4-review.blend`. The saved camera view is already set up. No Python packages, scripts, add-ons, paid plugins or re-render are required.

These are examples to adapt after discovering the real paths. Quote paths correctly; do not copy placeholder paths literally.

### macOS launch example

```sh
PACK_ROOT="/actual/path/to/Billeaford-Hall-full-review"
BLENDER_APP="/actual/path/to/Blender.app"
"$BLENDER_APP/Contents/MacOS/Blender" --version
open -a "$BLENDER_APP" "$PACK_ROOT/output/V4/model/garage-V4-review.blend"
open "$PACK_ROOT/START-HERE.html"
```

### Windows PowerShell launch example

```powershell
$PackRoot = 'C:\actual\path\Billeaford-Hall-full-review'
$BlenderExe = 'C:\actual\path\blender.exe'
$ModelPath = Join-Path $PackRoot 'output\V4\model\garage-V4-review.blend'
& $BlenderExe --version
Start-Process -FilePath $BlenderExe -ArgumentList ('"{0}"' -f $ModelPath)
Start-Process (Join-Path $PackRoot 'START-HERE.html')
```

### Linux launch example

```sh
PACK_ROOT="/actual/path/to/Billeaford-Hall-full-review"
BLENDER_EXE="/actual/path/to/blender"
"$BLENDER_EXE" --version
"$BLENDER_EXE" "$PACK_ROOT/output/V4/model/garage-V4-review.blend" &
xdg-open "$PACK_ROOT/START-HERE.html"
```

Use supported app-launch/UI tools instead of these commands if required by the agent's environment. If opening a local HTML file is blocked by that environment's policy, give Dad the file path to open himself; do not bypass the block. The browser viewer embeds its model and needs no server or external JavaScript download.

## 4. Verify and explain

Check that Blender opened `garage-V4-review.blend`, not its empty default scene or an old P02/V3 option. The default view should show one enclosed left bay with paired doors and two open bays, no vehicle, natural timber and a red roof. The scene contains `START HERE - V4 confirmed and provisional` as a Blender text block.

If direct screen inspection is available, verify the window/filename and view. Otherwise say what command/process was launched and ask Dad to confirm any first-use prompt. Do not report a visible window on the strength of an exit code alone.

Explain the pending heights before he measures the model: 4.163 m ridge, 2.300 m eaves and 0.300 m plinth are inherited placeholders. The 9 x 6 m footprint is agreed design intent; placement and ground levels remain unverified. The browser viewer's roof/door/weatherboarding switches are the easiest way to inspect inside.

For Blender navigation, middle-mouse drag normally orbits, scroll zooms and Shift + middle-mouse drag pans; use the viewport navigation controls on a trackpad. The browser viewer is a simpler alternative. It is fine to explain the supplied renders if Dad does not want to learn the modelling interface.

## Completion checklist

- Pack and current model located.
- Compatible Blender found or installed; actual version/path reported.
- Current model launched in the GUI, with the result honestly verified to the extent tools permit.
- Start page opened, or a precise path given if the environment prevents opening it.
- Project context and provisional dimensions explained.
- Original outputs preserved; no build scripts run as part of viewing setup.

If a step is blocked, complete the independent viewing/explanation steps and report the specific remaining action. Do not ask Dad to gather all the outstanding survey information just to inspect the pack.
