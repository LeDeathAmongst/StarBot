# s.flux (Hybrid Command)
Generate Images using Flux!<br/>

**Examples:**<br/>
- `s.flux cyberpunk cat`<br/>
- `s.f kermit --model=realism`<br/>

**Arguments:**<br/>
- `<prompt>` - A detailed description of the image you want to create.<br/>
- `--model` - Choose the specific model to use for image generation.<br/>
- `--size` - Aspect Ratio for the generated image.<br/>
- `--seed` - Specific seed value for randomization.<br/>

**Models:**<br/>
- `base` - Base flux model.<br/>
- `realism` - Flux model with a LORa fine tuned for realism.<br/>
- `3d` - Flux model with a LORa fine tuned for 3d images.<br/>
- `anime` - Flux model with a LORa fine tuned for anime.<br/>
- `disney` - Flux model with a LORa fine tuned for disney.<br/>
 - Usage: `s.flux <args>`
 - Slash Usage: `/flux <args>`
 - Aliases: `f`
Extended Arg Info
> ### args: str
> ```
> A single word, if not using slash and multiple words are necessary use a quote e.g "Hello world".
> ```
