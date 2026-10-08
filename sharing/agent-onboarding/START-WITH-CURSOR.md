# Start this pack with Cursor

1. Download and **extract/unzip the complete pack**. Keep all its folders together.
2. In Cursor, open the folder containing `AGENTS.md` and `START-HERE.html` as your project folder. Use a **local Agent chat on your computer**, so it can install and open desktop apps there.
3. Paste the prompt below into Agent and send it. Allow any tool or operating-system permission it needs for the requested setup.

## Copy this prompt

```text
Start this garage review pack for me. Read AGENTS.md and LLM-PROJECT-CONTEXT.md first, then follow SETUP-BLENDER.md. Check whether a compatible Blender is already installed; if not, install the free official Blender version suitable for this computer. Open output/V4/model/garage-V4-review.blend in Blender and open START-HERE.html in my browser. Do not rebuild or overwrite the supplied files. Verify what opened, explain the project and what I am looking at in plain English, and tell me which dimensions or site details are still provisional. Then help me inspect it and answer my questions.
```

The pack includes `AGENTS.md` and an always-applied Cursor project rule under `.cursor/rules/`. These give Agent the project instructions; **opening a folder alone does not start an installation or open the model**. The prompt starts that work. If Agent seems unaware of the instructions, explicitly attach `AGENTS.md` and `LLM-PROJECT-CONTEXT.md` to the chat. [Cursor's rules documentation](https://cursor.com/docs/rules).

## What should happen

- Agent reads the project context, finds or installs Blender, and opens the current V4 model.
- It opens the review page containing the interactive viewer, PDFs, pictures and project notes.
- It explains that the 9 x 6 m layout and appearance are agreed, while the model's roof/plinth dimensions and the actual site position are still provisional.

The files are ready to inspect. No code build or long render is needed to open them. Internet is needed only if Blender must be downloaded; the supplied browser viewer and documents work from the extracted folder.

## Things you can ask afterwards

- “Talk me through this model and show me where the enclosed bay is.”
- “What is agreed, and what are we still waiting for?”
- “Show me the framing with the roof off.”
- “Why does the model still show a 4.163 m ridge?”
- “Compare the current design with the earlier proposed drawing.”
- “Here are my measurements and sketch. Record what they confirm and what still needs checking.”

Cursor may not be able to see your live Blender view. If you mean a particular object or angle, name it or provide a screenshot. Agent can also use the supplied pictures and model records to explain the design.

If installing Blender is blocked, open `START-HERE.html` yourself and use **Open the interactive 3D garage**. You can rotate it and hide the roof, doors or weatherboarding without Blender.
