---
name: genai-video
description: Make an ad or short film from generated footage, covering script, cast, stills, takes, voice, graphics, a code edit, machine checks and the production log. Use for any video whose pictures come from an image or video model.
---

# GenAI Video

How to make a video ad or short film whose footage is generated. The method covers the
whole job: what to settle before any model runs, how to shoot, how to edit, how to check
a file the agent cannot watch or hear, and what to write down so the next agent can pick
the work up.

**Evidence and limits.** These rules come from one finished spot: a 39-second
talking-pitchman ad with a period television look, taken through four cuts in about a
day. One spot is a small sample. Rules marked "one test" rest on a single comparison.
Models change quickly, so re-test model behaviour on each new video and update this file
when a new production teaches something different.

## When to invoke

- A video ad, spot, infomercial, character film or social video made from generated
  stills and generated footage
- Revising a generated-footage cut after notes
- Adding a generated character, voice or scene to an otherwise designed video

Not for videos drawn entirely in code with no generated footage, and not for editing a
video file someone supplied.

## Order of work

Nothing goes to a video model until steps 1 to 5 are approved. On the first spot a
video take cost about twenty times what a still cost, so fix problems while they are
stills.

1. **Research.** Reference ads and why they worked, the audience, the one idea. Sources
   inline.
2. **Script.** One idea that fits in a sentence. Write the timed treatment with
   `craft/compound-copywriting/references/video-treatments.md`. Read it aloud to time
   it. One spoken line per shot.
3. **Shot list.** One row per shot: line, length, framing, action, what is added in the
   edit, sound.
4. **Cast and look.** Offer a few character options, let the human pick one, then make
   one character sheet. Collect the human's reference images for the look.
5. **Stills.** One approved still (a plate) per shot, each made from the character
   sheet so the person stays the same. Lay them out in order. A film that fails as
   stills is not rescued by motion.
6. **Model test.** Run one shot through two video models with the same plate and line
   before committing. Ask the human which they prefer, and which part they like:
   picture, voice or movement.
7. **Takes.** Shot by shot. Check each take by machine before it enters the cut.
8. **Graphics.** Titles, logos, prices and end cards are made in code, not generated.
9. **Edit.** In code, so each note is a re-run.
10. **Checks.** Measure the finished file, then run review models and measure what they
    claim.
11. **Log.** Update the production log.

Untried on the first spot and worth testing: an animatic (stills cut to a voice track)
before paying for takes.

## Stills and takes

- **Video models never draw anything that must be exact.** No logos, prices, phone
  numbers or type in generated footage. End every take prompt with a line saying no
  text, captions, subtitles or logos appear anywhere.
- **Exception: text that must move with a prop.** Print it into the plate, and tell the
  take prompt the lettering stays exactly as in the image and never changes or blurs.
- **Anything replaced later is flat green in the plate.** A screen, a sign, a whole
  backdrop. Tell the take prompt it stays flat, solid green for the whole clip and
  nothing ever appears on it.
- **One shot, one action.** Keep the camera locked off unless the move is the point.
  Pushes, zooms and pans are steadier and free when done in the edit.
- **Keep the person the same.** Every plate comes from the one character sheet, and
  every take prompt says to keep the same face, clothes and set as the image.
- **Use invented people,** or a person who has agreed to be filmed. Never another real
  person's face.
- **Expect several tries per shot.** One line needed five takes to hold an accent;
  another needed three to pronounce one word. When a word keeps going wrong, spell out
  the fix in the prompt.
- **Shoot at draft resolution first.** Draft footage warps hands, teeth and faces in
  places, and editing does not fix that. Get the cost of a full-resolution re-shoot
  before promising one.

### Take prompt shape

```
The [person] in the image is [who they are, in one phrase]. They say straight
into the camera, word for word: "[LINE]" [Call out any word the model gets wrong.]
Exactly the same voice and accent as the reference audio: [voice description:
age, texture, accent, delivery, recording setting].
Big, clearly articulated mouth movements. [One action, tied to a word in the
line.] [What must stay still or stay green.] Locked-off camera, no camera
movement, no cuts. Keep the same face, clothes and set as the image. [The look.]
No text, captions, subtitles or logos appear anywhere.
```

Inputs: the plate as the image, a reference voice clip as the audio, a duration of a few
seconds, and the aspect ratio of the final cut.

## Voice

- **Ask which layer the human liked before replacing anything.** On the first spot the
  approved voice was the video model's own voice on each take, not the separate
  voice-model recording. Replacing it was the largest mistake of the production.
- **Do not dub and lip-sync footage that already talks.** One clean recorded voice
  lip-synced onto every shot was rejected by the human and made the picture feel shaky.
- **What worked:** each take's own sound is the voice. A recorded line, or the sound of
  an earlier good take, goes in only as a reference that steers the take. It is never
  in the cut.
- **The cost of that choice:** the voice is not identical from shot to shot, because
  every take is voiced fresh. Say so at delivery.
- **Hold an accent with the prompt and the reference together,** then check every take
  with a listening model. The accent drifted until the voice description named it.
- **One test:** given the same plate and recorded line, one video model kept the
  recorded voice and another re-voiced the line itself. Find out which behaviour a
  model has before choosing it.

## Graphics and brand artwork

- **Get brand artwork from the human.** The logo on the live site was not the one the
  human meant.
- **Give each logo its own input to the edit,** so it can be swapped without touching
  anything else. Never redraw a logo.
- **The brand's own colours, fonts and logo files apply by default.** Set colours and
  fonts aside for a period look only when the human says so for that video. Logo files
  stay official either way.
- Draw titles and end cards in code to match the human's reference images. Let titles
  grow in and settle; do not pop them on.
- Keep stand-in values plainly fake until the true value exists, such as a phone number
  from a range reserved for fiction.
- When a value is baked into a graphics image, record its font, size, colour and
  position so it can be swapped later without a redraw.

## Edit

Edit in code. A re-render took one to two minutes and cost nothing, so every note was
one more run. Keep speed, sound levels, filters and per-join timings in settings, not in
the code.

- **Pick the output frame rate so each source frame shows once.** Footage at 24 frames a
  second, sped up 1.25 times, is 30 frames a second. A 1.12 times speed-up at 24 dropped
  frames and read as shaky.
- **No freeze frames and no reversed footage.** Both were used to fill time and both
  read as generated.
- **If the style has transitions, leave no hard cuts.** Put a move at every scene
  change.
- **Takes that talk from first frame to last leave no room for overlapping
  transitions.** Use moves that show one picture at a time, or keep overlaps shorter
  than the silence at each end. Print the gap between each take's last word and the
  next take's first in the render log.
- **Sound effects sit about 12 dB under the voice** and start a moment before the
  picture changes.
- **Do not end on silence.** Close with a short end card and a music swell.
- **Texture effects must not look like text.** A noise strip along the bottom of the
  frame read as garbled type.
- List anything added without being asked (sound effects, sparkles, extra headers) in
  the delivery note so the human can strike it.

## Checks

The agent cannot hear or watch playback. Say that in every delivery, and say what was
checked by machine in its place.

On every take, before it enters the cut:

- A listening model for the exact words, their times and the accent
- A second transcript from a different model
- Median pitch per clip when comparing two voices

On every cut:

- Hard cuts: frame-to-frame difference across every consecutive pair of frames
- Sound: peak level and clipped samples, and the loudness profile compared with the last
  cut when the sound should not have changed
- Still frames at each graphic's moments, looked at closely, for every placement of
  every logo
- Word gaps at each join

Review models:

- A watching model and a listening model on the finished cut produce leads, not
  findings. Measure each claim before acting. On the first spot the watching model
  reported frozen or reversed footage at four places, and measurement showed none.
- When only one layer changed, say which checks were re-run and which carry over from
  the last cut.

Report in three parts: checked by machine, raised by review models but not confirmed,
not checked.

## Revision rounds

- Before each round, re-read the shared notes for requests that arrived somewhere else.
  A logo request waited seven hours because the working session did not look.
- Record the human's notes word for word with the time. Earlier notes stay in force
  until reversed.
- Change the layer the note is about and nothing else.
- "Feels shaky" or "feels generated" is a symptom. Find the causes by measuring: frame
  rate, freezes, reversed clips, lip-sync, hard cuts. List each cause with its fix.
- Give each cut a version number and a link, and keep links to replaced cuts.

## Money and services

- Before a round of takes, say how many takes it is likely to need and what that costs.
  Read spend from the tool's usage report, not from memory.
- Before proposing a paid service, read its price on its own page that day, and check
  what the company already runs.
- Fix the bar for "free" or "works" before searching, and report each option against it.

## Clearance

Raise these early, not at the final cut, and run `launches/claims-clearance/SKILL.md`
before anything is public:

- Third-party logos: written permission
- Colleagues or customers on screen: their agreement
- Sensitive phrasing: editorial sign-off
- Prices and offers: confirmed by their owner, with an end date for any limited-time line
- Any claim on screen that is not on the live product page

Keep the cut internal until these close.

## The production log

Keep one log per video, in the project's own workspace and not in this repository. It
holds:

- Current cut: link, length, size, frame rate, status, who has seen it
- The human's direction in force, quoted
- What is in the cut, shot by shot, with lines and times
- How the cut is built, with the inputs and where they live
- Checked, not confirmed, not checked
- Limits, such as draft resolution or anything that depends on one machine
- What is on screen on the human's word only
- Open items and who owns them
- What was learned

## Dependencies

- `foundation/marketing-os`
- `craft/compound-copywriting/references/video-treatments.md` (script and treatment)
- `craft/art-direction` (look, references, brand artwork)
- `launches/claims-clearance/SKILL.md` (before a public release)
- `foundation/marketing-os/references/learning-loop.md` (when a production teaches
  something new)

## Quick checklist

- [ ] Script, shot list, character and stills approved before any video take
- [ ] One shot tested in two video models, and the human asked which layer they prefer
- [ ] No logos, prices or type in generated footage; replaced areas are flat green
- [ ] Every take checked for words and accent before it enters the cut
- [ ] Each take's own sound is the voice; no dub or lip-sync over talking footage
- [ ] Brand artwork came from the human and is a separate input to the edit
- [ ] Output frame rate shows each source frame once; no freezes or reversed footage
- [ ] Hard cuts, sound levels, logo placements and word gaps measured on the final file
- [ ] Review-model claims measured before acting
- [ ] Delivery says what was checked, what was not, and what was added unasked
- [ ] Clearance items raised and the production log updated
