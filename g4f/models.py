from g4f import Provider


class Model:
    class model:
        name: str
        base_provider: str
        best_provider: str

    class gpt_35_turbo:
        name: str = 'gpt-3.5-turbo'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        
    class gpt_35_turbo_0301:
        name: str = 'gpt-3.5-turbo-0301'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera

    class gpt_35_turbo_0613:
        name: str = 'gpt-3.5-turbo-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Phind
    
    class gpt_35_turbo_poe:
        name: str = 'gpt-3.5-turbo-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera

    class gpt_35_turbo_16k:
        name: str = 'gpt-3.5-turbo-16k'
        base_provider: str = 'reversed'
        best_provider: Provider.Provider = Provider.Chimera
    
    class gpt_35_turbo_16k_0613:
        name: str = 'gpt-3.5-turbo-16k-0613'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class gpt_35_turbo_16k_poe:
        name: str = 'gpt-3.5-turbo-16k-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        
    class gpt_4:
        name: str = 'gpt-4'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Chimera
        best_providers: list = [Provider.Bing, Provider.BingHuan, Provider.Chimera]
        
    class gpt_4_0314:
        name: str = 'gpt-4-0314'
        base_provider: str = 'reversed'
        best_provider: Provider.Provider = Provider.Chimera

    class gpt_4_poe:
        name: str = 'gpt-4-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera
        
    class gpt_4_32k:
        name: str = 'gpt-4-32k'
        base_provider: str = 'reversed'
        best_provider: Provider.Provider = Provider.Chimera
        
    class gpt_4_32k_poe:
        name: str = 'gpt-4-32k-poe'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera

    class claude_1:
        name: str = 'claude-1'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Slack
       
    class claude_instant_100k:
        name: str = 'claude-instant-100k'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera

    class claude_instant:
        name: str = 'claude-instant'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera
        
    class claude_2:
        name: str = 'claude-2'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.ClaudeAI
    
    class claude_2_100k:
        name: str = 'claude-2-100k'
        base_provider: str = 'anthropic'
        best_provider: Provider.Provider = Provider.Chimera
        
    class bloom:
        name: str = 'bloom'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class flan_t5_xxl:
        name: str = 'flan-t5-xxl'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class gpt_neox_20b:
        name: str = 'gpt-neox-20b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class oasst_sft_4_pythia_12b_epoch_35:
        name: str = 'oasst-sft-4-pythia-12b-epoch-3.5'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class oasst_sft_1_pythia_12b:
        name: str = 'oasst-sft-1-pythia-12b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class santacoder:
        name: str = 'santacoder'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.Vercel

    class command_light_nightly:
        name: str = 'command-light-nightly'
        base_provider: str = 'cohere'
        best_provider: Provider.Provider = Provider.Vercel

    class command_nightly:
        name: str = 'command-nightly'
        base_provider: str = 'cohere'
        best_provider: Provider.Provider = Provider.Vercel

    class text_ada_001:
        name: str = 'text-ada-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_babbage_001:
        name: str = 'text-babbage-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_curie_001:
        name: str = 'text-curie-001'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_davinci_002:
        name: str = 'text-davinci-002'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel

    class text_davinci_003:
        name: str = 'text-davinci-003'
        base_provider: str = 'openai'
        best_provider: Provider.Provider = Provider.Vercel
        
    class palm:
        name: str = 'palm'
        base_provider: str = 'google'
        best_provider: Provider.Provider = Provider.Poe
    
    class falcon_40b:
        name: str = 'falcon-40b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
    
    class falcon_7b:
        name: str = 'falcon-7b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
        
    class llama_13b:
        name: str = 'llama-13b'
        base_provider: str = 'huggingface'
        best_provider: Provider.Provider = Provider.H2o
        
    class sage:
        name: str = 'sage'
        base_provider: str = 'poe'
        best_provider: Provider.Provider = Provider.Chimera

    class llama_2_7b_chat:
        name: str = 'llama-2-7b-chat'
        base_provider: str = 'replicate'
        best_provider: Provider.Provider = Provider.Chimera

    class llama_2_13b_chat:
        name: str = 'llama-2-13b-chat'
        base_provider: str = 'replicate'
        best_provider: Provider.Provider = Provider.Chimera

    class llama_2_70b_chat:
        name: str = 'llama-2-70b-chat'
        base_provider: str = 'replicate'
        best_provider: Provider.Provider = Provider.Chimera

    class dall_e:
        name: str = 'dall-e'
        base_provider: str = 'Bing'
        best_provider: Provider.Provider = Provider.BingImg

    class kandinsky:
        name: str = 'kandinsky'
        base_provider: str = 'Fusionbrain'
        best_provider: Provider.Provider = Provider.Fusionbrain
    
    class bing:
        name: str = 'bing'
        base_provider: str = 'Bing'
        best_provider: Provider.Provider = Provider.Bing
        
class ModelUtils:
    convert: dict = {
        'gpt-3.5-turbo': Model.gpt_35_turbo,
        'gpt-3.5-turbo-0301': Model.gpt_35_turbo_0301,
        'gpt-3.5-turbo-0613': Model.gpt_35_turbo_0613,
        'gpt-3.5-turbo-poe': Model.gpt_35_turbo_poe,
        'gpt-3.5-turbo-16k': Model.gpt_35_turbo_16k,
        'gpt-3.5-turbo-16k-0613': Model.gpt_35_turbo_16k_0613,
        'gpt-3.5-turbo-16k-poe': Model.gpt_35_turbo_16k_poe,
        
        'gpt-4': Model.gpt_4,
        'gpt-4-0314': Model.gpt_4_0314,
        'gpt-4-poe': Model.gpt_4_poe,
        'gpt-4-32k': Model.gpt_4_32k,
        'gpt-4-32k-poe': Model.gpt_4_32k_poe,
        
        'claude-1': Model.claude_1,
        
        'claude-instant-100k': Model.claude_instant_100k,
        'claude-instant': Model.claude_instant,
        'claude-2': Model.claude_2,
        'claude-2-100k': Model.claude_2_100k,
        
        'bloom': Model.bloom,
        
        'flan-t5-xxl': Model.flan_t5_xxl,
        
        'gpt-neox-20b': Model.gpt_neox_20b,
        'oasst-sft-4-pythia-12b-epoch-3.5': Model.oasst_sft_4_pythia_12b_epoch_35,
        'oasst-sft-1-pythia-12b': Model.oasst_sft_1_pythia_12b,
        'santacoder': Model.santacoder,
        
        'command-light-nightly': Model.command_light_nightly,
        'command-nightly': Model.command_nightly,
        
        'text-ada-001': Model.text_ada_001,
        'text-babbage-001': Model.text_babbage_001,
        'text-curie-001': Model.text_curie_001,
        'text-davinci-002': Model.text_davinci_002,
        'text-davinci-003': Model.text_davinci_003,
        
        'palm2': Model.palm,
        'palm': Model.palm,
        'chat-bison-001': Model.palm,
        'google': Model.palm,
        'google-bard': Model.palm,
        'google-palm': Model.palm,
        'bard': Model.palm,
        
        'falcon-40b': Model.falcon_40b,
        'falcon-7b': Model.falcon_7b,
        'llama-13b': Model.llama_13b,

        'sage': Model.sage,
        'llama-2-7b-chat': Model.llama_2_7b_chat,
        'llama-2-13b-chat': Model.llama_2_13b_chat,
        'llama-2-70b-chat': Model.llama_2_70b_chat,
        'dall-e': Model.dall_e,
        'kandinsky': Model.kandinsky,
        'bing': Model.bing
    }