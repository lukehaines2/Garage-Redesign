# Billeaford Hall garage review - instructions for an AI agent

You are helping Dad inspect and discuss his garage replacement project. Treat the extracted folder containing this file as the pack root. Use paths relative to that folder; never assume Luke's original Mac paths exist here.

## Start the pack when asked

When Dad asks to start, run, open or set up this review pack, carry out the following workflow. Do the work, rather than just listing commands for him. A request to explain a detail does not require repeating setup.

1. Read `LLM-PROJECT-CONTEXT.md`, `output/V4/model/README.txt`, and the current V4 decisions at the top of `PROJECT_BRIEF.md`. Consult `WORK_STATUS.md` and `MEASUREMENTS_FOR_DAD.md` for the remaining inputs.
2. Confirm the pack is fully extracted and `output/V4/model/garage-V4-review.blend` exists. If the user opened its parent folder, locate the child containing `START-HERE.html` and work there.
3. Detect the operating system/architecture and check for an installed compatible Blender. Follow `SETUP-BLENDER.md`. Reuse Blender 4.5 or newer when suitable; otherwise install the free official Blender 4.5 LTS release for this machine. The starter prompt explicitly requests this installation if needed. Use normal tool/OS permissions and let the user handle any required administrator or first-launch prompt.
4. Launch the **Blender GUI with `output/V4/model/garage-V4-review.blend`**. Also open `START-HERE.html` in the default browser, so the user can inspect the pack without learning Blender first. The 3D browser viewer is `output/V4/viewer/garage-V4-viewer.html`.
5. Verify what actually happened. Check the opened filename/window when your tools allow; otherwise report that you launched the file and identify any confirmation still needed. Do not claim you saw the model on screen if you only started a process.
6. Give a short plain-English orientation: the current V4 design, how to rotate/inspect it, what the provisional dimensions mean, and where the earlier drawings are. Be ready to answer Dad's questions using the actual files.

Opening this folder does not itself run an installer. Start after the user invokes the workflow. If a permission, download, unsupported OS or graphics issue blocks Blender, explain the concrete issue and continue opening the supplied browser viewer, pictures and notes where possible. Do not bypass an OS security warning or pretend the install succeeded.

## Understand the scope before answering

- This is a **review pack**, not a completed planning application or construction set.
- The agreed proposal is a private-household garage at Billeaford Hall, Sloe Lane, Knodishall, IP17 1UU: 9 x 6 m, entrance east, three equal bays, the left bay enclosed with paired doors and a full dividing wall, two open bays, natural timber and red clay pantiles.
- The model's **4163 mm ridge, 2300 mm eaves and 300 mm plinth are retained placeholders**. They are not the newly agreed low-height design. Its three graphical brick courses within 300 mm do not specify real 100 mm brick courses.
- The model's equal front clear openings are 2800 mm using assumed 150 mm posts. Actual structural details remain unresolved. Its flat ground is a studio surface; the reported 300-400 mm courtyard fall has not been surveyed or modelled.
- Current V4 records supersede conflicting P02/V3 text. P02 drawings and V3 options are historical references. Some historical title blocks concern a different reference project; they do not establish this site's address or orientation.
- The old mapping screenshot is uncalibrated. Do not infer dimensions, ownership, north or accurate new-building position from its pixels. The licensed map, boundary annotations, sketches, photos and measurements are still awaited.

For fuller context and a file map, read `LLM-PROJECT-CONTEXT.md`. For legal/planning questions, use `output/V4/HEIGHT_AND_CONSTRUCTION.md` as dated research, verify current official requirements where needed, and distinguish national rules from this site's unverified eligibility.

## Answer questions from evidence

Use the V4 renders or accepted illustration when explaining appearance, the saved model/verification report when explaining model geometry, and the current brief when explaining intent. A `.blend` is a binary project, not a text document. If necessary inspect it through Blender's Python API using the discovered Blender executable; read-only queries are enough for most questions. Do not guess geometry from a filename.

If Dad asks what he is looking at, identify the file/version and viewpoint first. Describe the visible feature, explain its purpose, then say whether it is agreed, a model assumption or unresolved. If you cannot see his current Blender view/selection, use the known render or ask which view/part he means; do not claim Cursor automatically sees another application's screen.

Useful explanation: looking at the east-facing entrance, the enclosed bay is on the left (south end in this model); the two bays to its right are open. The full partition extends up into the roof. Hiding the roof or weatherboarding in the browser viewer exposes illustrative interior framing, not verified structural engineering.

## Preserve the supplied review set

- **Opening the pack does not require running any build scripts**, installing Python dependencies, rendering, starting a server, or rebuilding every version. Open the supplied outputs first. Installation of Blender does not require a paid service, model plugin or add-on.
- Keep the supplied V4 model and historical P02/V3 outputs intact. For requested edits, save a new working copy in `output/Working/` and record what changed. Do not silently run `scripts/blender_scene.py`, `scripts/v3_scene.py` or `scripts/v4_scene.py`: they generate/overwrite outputs.
- The included `scripts/package_full_review.py` is Luke's packaging utility; it expects the original archives in his working project. Do not run it to launch this extracted pack.
- Capture new decisions or measurements supplied by Dad in `DAD-REVIEW-NOTES.md`, distinguishing measured/estimated/unknown and the date/source. Explicit new decisions can update the current brief; do not rewrite historical records or promote estimates to surveyed facts.
- Preparing local review material does not authorise purchases, messages to other people, appointments, public uploads or a planning submission. Follow Dad's actual instructions and your environment's permission rules.

## Finish setup with a useful result

Tell Dad the Blender version found/installed, which model was opened, where the browser review page is, and any actual blocker. Briefly identify the unresolved roof/plinth/site information. Then help him inspect the project; do not repeatedly run the installer on later questions.
