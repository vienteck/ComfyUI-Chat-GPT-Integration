# Credits to Omar92. This is based heavily off of his code
https://github.com/omar92/ComfyUI-QualityOfLifeSuit_Omar92 

I rewrote the core logic because this code was not compaitible with the new version of the OpenAi api

# ComfyUI-ChatGPTIntegration
Single node to prompt ChatGPT and will return an input for your CLip TEXT Encode Prompt

## ComfyUI
ComfyUI is an advanced node-based UI that utilizes Stable Diffusion, allowing you to create customized workflows such as image post-processing or conversions.

## How to install
Download the zip file.
Extract to ..\ComfyUI\custom_nodes.
Restart ComfyUI if it was running (reloading the web is not enough).
You will find my nodes under the new group O/....

## How to update
- No Auto Update

The file looks like this :

{
"openAI_API_Key": "sk-#################################"
}

## ChatGPTPrompt
This node harnesses the power of chatGPT, an advanced language model that can generate detailed image descriptions from a small input.
- you need to have  OpenAI API key , which you can find at https://beta.openai.com/docs/developer-apis/overview
- Once you have your API key, add it to the `config.json` file
- I have made it a separate file, so that the API key doesn't get embedded in the generated images.


## Contact
### Discord: vienteck#6218
### GitHub: vienteck (https://github.com/vienteck)