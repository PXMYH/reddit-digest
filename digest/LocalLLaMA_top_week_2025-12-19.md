# r/LocalLLaMA Reading Digest

**Period:** 2025-12-19 to 2025-12-19
**Posts Summarized:** 50
**Total Posts Analyzed:** 50

---

## 1. [Kimi K2 Thinking at 28.3 t/s on 4x Mac Studio cluster](https://reddit.com/r/LocalLLaMA/comments/1pq2ry0/kimi_k2_thinking_at_283_ts_on_4x_mac_studio/)

**Author:** u/geerlingguy | **Upvotes:** 477 | **Comments:** 131 | **Date:** 2025-12-18

**Summary:** The post discusses performance testing of Kimi K2 on a cluster of 4 Mac Studios using RDMA Tensor settings, highlighting the challenges in benchmarking and the potential for future improvements with new Apple Silicon chips.

**Key Points:**
- Testing Kimi K2 on a 4x Mac Studio cluster with RDMA Tensor settings.
- Challenges in benchmarking due to lack of tools like llama-bench in Exo.
- Potential for significant performance improvements with upcoming Apple Silicon ultra chips featuring MATMUL instructions.
- Community appreciation for the testing efforts and contributions.
- Additional data and context available via linked sources (blog post and GitHub issue).

**Discussion Highlights:** The discussion highlights community interest and appreciation for the testing efforts, with a focus on the potential for future performance improvements with new hardware. There is also a notable mention of additional resources for more detailed data.

---

## 2. [T5Gemma 2: The next generation of encoder-decoder models](https://reddit.com/r/LocalLLaMA/comments/1ppzhtq/t5gemma_2_the_next_generation_of_encoderdecoder/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 206 | **Comments:** 31 | **Date:** 2025-12-18

**Summary:** T5Gemma 2 models, based on Gemma 3, are multilingual and multimodal, handling text and image input with open weights for three pretrained sizes (270M, 1B, and 4B). They feature tied embeddings, merged attention, multimodality, extended long context, and support for over 140 languages.

**Key Points:**
- Tied embeddings reduce parameter count and improve memory efficiency
- Merged attention mechanism simplifies architecture and improves inference
- Multimodal capabilities for text and image processing
- Extended context window of up to 128K tokens
- Support for over 140 languages

**Discussion Highlights:** The community is excited about the new encoder-decoder model, with requests for larger models and GGUF support. There is enthusiasm for its potential in multimodal translation tasks.

---

## 3. [Google's Gemma models family](https://reddit.com/r/LocalLLaMA/comments/1ppun3v/googles_gemma_models_family/)

**Author:** u/jacek2023 | **Upvotes:** 470 | **Comments:** 114 | **Date:** 2025-12-18

**Summary:** The Reddit post discusses Google's Gemma models family, highlighting the introduction of FunctionGemma and community reactions.

**Key Points:**
- Introduction of FunctionGemma for fine-tuning
- Community excitement and humor about the new models
- Technical details and model count discussed
- Positive reception and special recognition for the post

**Discussion Highlights:** The community shows enthusiasm for FunctionGemma, with humorous remarks about the models becoming reality. Technical discussions include model counts and fine-tuning capabilities.

---

## 4. [MiraTTS: High quality and fast TTS model](https://reddit.com/r/LocalLLaMA/comments/1pper90/miratts_high_quality_and_fast_tts_model/)

**Author:** u/SplitNice1982 | **Upvotes:** 138 | **Comments:** 52 | **Date:** 2025-12-17

**Summary:** MiraTTS is a high-quality, fast TTS model that generates realistic 48khz speech at 100x realtime, optimized for efficiency and low latency. It supports multilingual versions and is memory-efficient, working with GPUs as low as 6GB VRAM.

**Key Points:**
- MiraTTS generates speech at 100x realtime with high quality and clarity.
- It is memory-efficient and works with GPUs having 6GB VRAM.
- Supports multilingual versions and aims for low latency (as low as 150ms).
- The model is optimized using Lmdeploy and FlashSR for audio enhancement.
- Multispeaker support is in progress and expected soon.

**Discussion Highlights:** The discussion highlights curiosity about multilingual support, voice cloning, and comparisons with other TTS models like KaniTTS. Users appreciate the frequent releases and express interest in trying the model, though some face hardware limitations.

---

## 5. [AMA with the Meta researchers behind SAM 3 + SAM 3D + SAM Audio](https://reddit.com/r/LocalLLaMA/comments/1pp9w31/ama_with_the_meta_researchers_behind_sam_3_sam_3d/)

**Author:** u/AIatMeta | **Upvotes:** 129 | **Comments:** 73 | **Date:** 2025-12-17

**Summary:** The post announces an AMA with Meta researchers behind the new Segment Anything models: SAM 3, SAM 3D, and SAM Audio. The team introduces the models, provides links for further information, and invites users to test them in the Segment Anything Playground.

**Key Points:**
- Introduction of SAM 3, SAM 3D, and SAM Audio models by Meta researchers
- Team members from each model are listed and available for the AMA
- Users can test the models in the Segment Anything Playground
- Top comments discuss model capabilities, architecture, and potential applications
- AMA concludes with gratitude for user participation

**Discussion Highlights:** Users inquired about model capabilities, such as segmenting multiple objects, voice separation for home assistants, and architecture similarities across models. There was also interest in comparing SAM Audio to other tools like Demucs for stem creation and karaoke applications.

---

## 6. [Nvidia plans heavy cuts to GPU supply in early 2026](https://reddit.com/r/LocalLLaMA/comments/1pp8vo4/nvidia_plans_heavy_cuts_to_gpu_supply_in_early/)

**Author:** u/HumanDrone8721 | **Upvotes:** 343 | **Comments:** 173 | **Date:** 2025-12-17

**Summary:** Nvidia plans to significantly reduce GPU supply in early 2026, which, combined with similar cuts by Micron and Samsung, could make building gaming PCs challenging. The discussion highlights concerns about market competition and corporate spending priorities.

**Key Points:**
- Nvidia plans heavy cuts to GPU supply in early 2026
- Micron and Samsung are also cutting consumer RAM and SSD production
- 2026 may be a difficult year for building gaming PCs due to supply constraints
- Potential for new competition to emerge in the market
- Criticism of corporate stock buybacks over investment in growth

**Discussion Highlights:** The discussion reflects concerns about the impact of supply cuts on gaming PC builds and frustration with corporate practices like stock buybacks. Some users hope for increased competition in the market.

---

## 7. [Hey, LocalLLaMa. We need to talk...](https://reddit.com/r/LocalLLaMA/comments/1pp6jhq/hey_localllama_we_need_to_talk/)

**Author:** u/Eisenstein | **Upvotes:** 398 | **Comments:** 127 | **Date:** 2025-12-17

**Summary:** The post highlights the importance of engaging with and supporting contributors in the r/LocalLLaMA community by providing upvotes and constructive feedback. The discussion reveals mixed opinions, with some emphasizing engagement and others criticizing the quality of projects shared.

**Key Points:**
- The need for upvotes and feedback to encourage contributors
- Importance of constructive criticism for growth
- Value of engagement beyond just entertainment
- Mixed reactions in comments regarding project quality
- Consensus on the importance of community engagement

**Discussion Highlights:** The discussion shows a consensus on the value of engagement but differing opinions on the quality of projects being shared. Some commenters appreciate the call for support, while others criticize low-quality or AI-generated projects.

---

## 8. [Drummer's Cydonia and Magidonia 24B v4.3 - The best pair of Cydonia for RP yet!](https://reddit.com/r/LocalLLaMA/comments/1pp2j60/drummers_cydonia_and_magidonia_24b_v43_the_best/)

**Author:** u/TheLocalDrummer | **Upvotes:** 130 | **Comments:** 20 | **Date:** 2025-12-17

**Summary:** The post announces the release of Drummer's Cydonia and Magidonia 24B v4.3 models, described as the best pair for RP yet, with links to their respective Hugging Face repositories. The author expresses gratitude to patrons for their support and mentions a recent difficult choice made possible by their backing.

**Key Points:**
- Release of Cydonia-24B-v4.3 and Magidonia-24B-v4.3 models
- Models praised as the best for RP by testers at Beaver
- Author thanks patrons for their support and freedom granted
- Magidonia is preferred by most users, though both models are well-received
- Additional context provided on attaching vision mmproj to the gguf

**Discussion Highlights:** The discussion highlights appreciation for the author's contributions, with users expressing gratitude and interest in testing the models. Some comments provide technical details, such as attaching vision mmproj, and others share personal preferences for the Magidonia model.

---

## 9. [Apple introduces SHARP, a model that generates a photorealistic 3D Gaussian representation from a single image in seconds.](https://reddit.com/r/LocalLLaMA/comments/1poy0lb/apple_introduces_sharp_a_model_that_generates_a/)

**Author:** u/themixtergames | **Upvotes:** 1143 | **Comments:** 129 | **Date:** 2025-12-17

**Summary:** Apple has introduced SHARP, a model capable of generating photorealistic 3D Gaussian representations from a single image in seconds. The model is highlighted for its speed and compatibility with Apple devices like the MacBook Pro M1 Max and Apple Vision Pro.

**Key Points:**
- SHARP generates photorealistic 3D Gaussian representations from a single image in seconds.
- The model is optimized for Apple devices, with examples rendered in real-time on Apple Vision Pro.
- The GitHub repository and research paper are provided for further exploration.
- Community discussion includes comparisons to cyberpunk's braindance and inquiries about the model's capabilities.

**Discussion Highlights:** The community discussion highlights the model's speed and compatibility with Apple hardware, with some users drawing comparisons to futuristic technologies like cyberpunk's braindance. There is also curiosity about the model's limitations and potential applications.

---

## 10. [LangChain and LlamaIndex are in "steep decline" according to new ecosystem report. Anyone else quietly ditching agent frameworks?](https://reddit.com/r/LocalLLaMA/comments/1pox733/langchain_and_llamaindex_are_in_steep_decline/)

**Author:** u/Exact-Literature-395 | **Upvotes:** 204 | **Comments:** 57 | **Date:** 2025-12-17

**Summary:** The Reddit post discusses the decline of LangChain and LlamaIndex frameworks, citing reduced community activity and investment. Users share their experiences of moving away from these frameworks due to complexity and lack of necessity with improved base models.

**Key Points:**
- LangChain, LlamaIndex, and AutoGen are listed as 'steepest declining' projects by community activity.
- Users report better results by calling APIs directly instead of using these frameworks.
- Criticisms include bloated features, poor security/performance, and non-pythonic design choices.
- Some argue these frameworks may still be essential for complex workflows.
- The discussion reflects a broader trend of moving away from overly abstracted frameworks.

**Discussion Highlights:** The consensus among commenters is largely negative toward LangChain and similar frameworks, with many users expressing relief at moving away from them. The maintainer of LlamaIndex acknowledges the shift but highlights the frameworks' role in community integration. Overall, the discussion suggests a growing preference for simpler, more direct approaches to LLM development.

---

## 11. [anthropic blog on code execution for agents. 98.7% token reduction sounds promising for local setups](https://reddit.com/r/LocalLLaMA/comments/1powhy6/anthropic_blog_on_code_execution_for_agents_987/)

**Author:** u/Zestyclose_Ring1123 | **Upvotes:** 133 | **Comments:** 33 | **Date:** 2025-12-17

**Summary:** Anthropic's blog discusses a new approach to code execution for agents, claiming a 98.7% token reduction, which could significantly benefit local setups by reducing context limits and improving privacy. The approach involves letting models explore tools on demand rather than preloading all tool definitions.

**Key Points:**
- Anthropic's method reduces token usage by 98.7%, making it feasible for local models with limited context.
- The approach involves model-generated code that orchestrates tools, with data flowing through variables rather than context.
- Privacy is enhanced as sensitive data never enters the model context, flowing directly between tools.
- Sandboxing is a major challenge for running model-generated code locally.
- Similar patterns already exist in projects like HF's smolagents and other implementations.

**Discussion Highlights:** The discussion highlights that while Anthropic's approach is promising, similar patterns have been independently discovered and implemented by others, such as HF's smolagents. There is consensus on the potential benefits for local setups, but concerns about sandboxing and security remain. Some users have already experimented with similar patterns, using methods like generating a DAG of steps to reduce sandboxing needs.

---

## 12. [Peak LLM Wars: Xiaomi Blocks Kimi Employees on Twitter](https://reddit.com/r/LocalLLaMA/comments/1pow797/peak_llm_wars_xiaomi_blocks_kimi_employees_on/)

**Author:** u/nekofneko | **Upvotes:** 129 | **Comments:** 28 | **Date:** 2025-12-17

**Summary:** The Reddit post discusses the ongoing LLM wars, highlighting Xiaomi blocking Kimi employees on Twitter. The post includes images and comments that reflect the competitive and dramatic nature of the LLM industry.

**Key Points:**
- Xiaomi blocking Kimi employees on Twitter
- LLM wars and industry competition
- Meme format discussion in comments
- Speculation about former DeepSeek members in Xiaomi team
- Comparison to other industry beefs

**Discussion Highlights:** The discussion highlights the competitive nature of the LLM industry, with comments focusing on the meme format, speculation about team members, and comparisons to other industry rivalries.

---

## 13. [Microsoft's TRELLIS 2-4B, An Open-Source Image-to-3D Model](https://reddit.com/r/LocalLLaMA/comments/1porpwd/microsofts_trellis_24b_an_opensource_imageto3d/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 1141 | **Comments:** 120 | **Date:** 2025-12-17

**Summary:** Microsoft's TRELLIS 2-4B is an open-source image-to-3D model with 4 billion parameters, converting single images into 3D assets. The model uses Flow-Matching Transformers with Sparse Voxel based 3D VAE. Community feedback highlights mixed results and suggestions for improvement.

**Key Points:**
- Model Type: Flow-Matching Transformers with Sparse Voxel based 3D VAE
- Parameters: 4 Billion
- Input: Single Image, Output: 3D Asset
- Community feedback indicates mixed results and practical limitations
- Suggestions for improvement include using multiple images for better results

**Discussion Highlights:** The community discussion includes mixed reviews on the model's performance, with some users finding it excellent and others noting practical limitations. Suggestions for improvement include using multiple images for better results.

---

## 14. [QwenLong-L1.5: Revolutionizing Long-Context AI](https://reddit.com/r/LocalLLaMA/comments/1pokpha/qwenlongl15_revolutionizing_longcontext_ai/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 208 | **Comments:** 27 | **Date:** 2025-12-16

**Summary:** QwenLong-L1.5 is a new AI model achieving state-of-the-art long-context reasoning with novel data synthesis, stabilized RL, and memory management for contexts up to 4M tokens. The model is available on HuggingFace and has generated significant interest in the community.

**Key Points:**
- Achieves SOTA long-context reasoning with up to 4M tokens
- Uses novel data synthesis and stabilized RL techniques
- Available on HuggingFace for public use
- Community interest in integration with llama.cpp
- Importance of using the exact query template for optimal performance

**Discussion Highlights:** The community discussion highlights enthusiasm for the model's capabilities, with specific interest in its integration with existing tools like llama.cpp. There is also a focus on the importance of using the exact query template provided by the developers for best results. Some users expressed minor critiques about visual presentation in associated graphs.

---

## 15. [8x Radeon 7900 XTX Build for Longer Context Local Inference - Performance Results &amp; Build Details](https://reddit.com/r/LocalLLaMA/comments/1pogwb6/8x_radeon_7900_xtx_build_for_longer_context_local/)

**Author:** u/Beautiful_Trust_8151 | **Upvotes:** 720 | **Comments:** 211 | **Date:** 2025-12-16

**Summary:** The post describes an 8x Radeon 7900 XTX GPU build for local AI inference, achieving 192 GB VRAM and stable performance with up to 200+ tokens per second during prompt processing. The setup costs around $6-7k and offers flexibility for long-context AI tasks.

**Key Points:**
- 8x AMD Radeon 7900 XTX GPUs with 192 GB VRAM total, paired with an Intel Core i7-14700F and 192 GB system RAM.
- Performance results show 437 tokens/sec (empty context) and 200+ tokens/sec (19k tokens), with stable operation.
- Total build cost is ~$6-7k, offering a budget-friendly alternative to professional GPUs like RTX Pro 6000.
- Community appreciates the build as a notable example of early AI era hardware experimentation.
- Suggestions for testing other models like Qwen3-235B-A22B to further evaluate performance.

**Discussion Highlights:** The community praised the build as a cost-effective and flexible solution for long-context AI inference, comparing it to early industrial-era innovations. Some users suggested additional benchmarks with other models, while others noted the complexity of managing such a setup compared to professional-grade hardware.

---

## 16. [Nemotron 3 Nano 30B is Amazing! (TLDR)](https://reddit.com/r/LocalLLaMA/comments/1pocsdy/nemotron_3_nano_30b_is_amazing_tldr/)

**Author:** u/DonkeyBonked | **Upvotes:** 201 | **Comments:** 128 | **Date:** 2025-12-16

**Summary:** The Reddit post discusses the user's experience with Nemotron 3 Nano 30B, highlighting its impressive token efficiency and performance on their unique hardware setup. The user compares it favorably to other models like Devstral 2 Small 24B and Qwen models, noting its ability to handle large contexts efficiently.

**Key Points:**
- Nemotron 3 Nano 30B shows high token efficiency, fitting 256k tokens in VRAM and handling up to 1M context with spillover.
- The model performs well on the user's hardware setup, which includes an RTX 5000 and an RTX 3090 eGPU.
- Comparisons with other models like Devstral 2 Small 24B and Qwen models show Nemotron 3 Nano 30B's superior performance in certain tasks.
- Users in the comments discuss the model's speed, performance, and open-source nature, with some preferring Qwen models for specific use cases.
- The model is praised for its ability to generate functional code and follow instructions effectively.

**Discussion Highlights:** The discussion highlights a consensus on Nemotron 3 Nano 30B's impressive performance and token efficiency. Some users prefer it for its speed and open-source nature, while others still favor Qwen models for specific tasks like code generation. The model's ability to handle large contexts and perform well on varied hardware setups is a recurring theme.

---

## 17. [32GB Mi50's were getting so expensive that I ended up buying a 32GB w6800 for about the same price instead](https://reddit.com/r/LocalLLaMA/comments/1pob44f/32gb_mi50s_were_getting_so_expensive_that_i_ended/)

**Author:** u/EmPips | **Upvotes:** 229 | **Comments:** 42 | **Date:** 2025-12-16

**Summary:** The author opted for a 32GB w6800 GPU instead of a 32GB Mi50 due to similar pricing, highlighting the convenience and cooling performance of the w6800. The discussion includes comparisons with other GPUs like the AMD Radeon AI PRO R9700 and Zotac 3090s.

**Key Points:**
- Author chose 32GB w6800 over 32GB Mi50 due to similar pricing
- w6800 offers convenience and effective cooling
- Alternatives like AMD Radeon AI PRO R9700 and Zotac 3090s were mentioned
- Price comparisons and performance considerations were discussed

**Discussion Highlights:** The discussion revolves around the cost-effectiveness and performance of different GPUs, with users sharing their experiences and recommendations. The consensus leans towards considering alternatives like the w6800 for its convenience and cooling, while also acknowledging other options like the R9700 and 3090s.

---

## 18. [8 Million Users' AI Conversations Sold for Profit by "Privacy" Extensions | Koi Blog](https://reddit.com/r/LocalLLaMA/comments/1poal2a/8_million_users_ai_conversations_sold_for_profit/)

**Author:** u/ManThigh | **Upvotes:** 161 | **Comments:** 47 | **Date:** 2025-12-16

**Summary:** The Reddit post highlights privacy concerns regarding browser extensions selling AI conversation data of millions of users for profit, emphasizing the importance of using local models and auditing extensions.

**Key Points:**
- Browser extensions like Urban VPN Proxy and 1ClickVPN Proxy sold AI conversation data of millions of users.
- The post advises using local models and auditing extensions to protect privacy.
- User interactions with LLMs and browsing behavior are highly valuable data.
- Comments express outrage and suggest punishing companies that buy such data.
- Local setups are praised for avoiding such privacy risks.

**Discussion Highlights:** The discussion consensus emphasizes the need for privacy protection, criticizes companies involved in data sales, and advocates for local AI setups to avoid such risks.

---

## 19. [Finally managed to run Qwen-2.5-7B on a 4GB GTX 1050 without CPU offloading (Surgical Memory Alignment)](https://reddit.com/r/LocalLLaMA/comments/1po97ad/finally_managed_to_run_qwen257b_on_a_4gb_gtx_1050/)

**Author:** u/HuseyinKama | **Upvotes:** 144 | **Comments:** 48 | **Date:** 2025-12-16

**Summary:** The post discusses a method called 'Surgical Memory Alignment' to run Qwen-2.5-7B on a 4GB GTX 1050 without CPU offloading, saving VRAM and improving speed. The author open-sourced the solution as QKV Core.

**Key Points:**
- Standard GGUF quantization tools add padding that wastes memory, causing OOM errors on low-end GPUs.
- Surgical Alignment trims and realigns memory blocks to fit llama.cpp's boundaries, saving ~44MB per model.
- The method improved I/O load times by ~34% and kept the entire model on GPU.
- The solution is open-sourced as QKV Core for others with low-end GPUs.
- Discussion includes skepticism about the code and questions about the optimization process.

**Discussion Highlights:** The discussion includes praise for the optimization, skepticism about the code's effectiveness, and questions about how the optimization works and whether it creates new GGUF files.

---

## 20. [I was bored](https://reddit.com/r/LocalLLaMA/comments/1po8yt0/i_was_bored/)

**Author:** u/MyLovelyAngelKirino | **Upvotes:** 130 | **Comments:** 70 | **Date:** 2025-12-16

**Summary:** The author, who is unemployed with spare time and hardware, built a high-performance computer setup. The post garnered significant attention, with users admiring the hardware and joking about the author's resources.

**Key Points:**
- Author built a powerful computer setup with 3x 3090 GPUs, 512GB RAM, and an Epyc 7663 56-core CPU
- Post received 130 upvotes and 70 comments
- Community reactions included admiration, humor, and requests for more details
- Some users joked about the author's access to hardware and resources
- Discussion included questions about water-cooling components and GPU configuration

**Discussion Highlights:** The community expressed admiration for the setup's power and neatness, with some users humorously questioning how the author acquired such resources. There were also requests for more technical details about the build.

---

## 21. [Meta announced a new SAM Audio Model for audio editing that can segment sound from complex audio mixtures using text, visual, and time span prompts.](https://reddit.com/r/LocalLLaMA/comments/1po7i0c/meta_announced_a_new_sam_audio_model_for_audio/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 506 | **Comments:** 85 | **Date:** 2025-12-16

**Summary:** Meta has introduced a new SAM Audio Model that revolutionizes audio editing by enabling the isolation of specific sounds from complex audio mixtures using text, visual, and time span prompts.

**Key Points:**
- SAM Audio Model simplifies audio processing by isolating sounds from complex mixtures.
- The model uses text, visual, and time span prompts for sound segmentation.
- Potential applications include filtering out unwanted noises in virtual meetings.
- The model's effectiveness in isolating sounds from videos is highlighted as impressive.
- Discussion includes inquiries about the model's applicability to musical instruments.

**Discussion Highlights:** The discussion highlights the potential of the SAM Audio Model in practical applications like virtual meetings and its impressive capability to isolate sounds from videos. There is also interest in its applicability to musical instruments.

---

## 22. [Allen Institute for AI introduces Molmo 2](https://reddit.com/r/LocalLLaMA/comments/1po78bl/allen_institute_for_ai_introduces_molmo_2/)

**Author:** u/Agitated_Camel1886 | **Upvotes:** 240 | **Comments:** 22 | **Date:** 2025-12-16

**Summary:** The Allen Institute for AI has introduced Molmo 2, an 8B model capable of advanced video analysis tasks like Video QA, counting, pointing, and dense captioning. The community is impressed by its capabilities and the public release of datasets.

**Key Points:**
- Molmo 2 is an 8B model with advanced video analysis capabilities.
- The model supports tasks like Video QA, counting, pointing, and dense captioning.
- Allen AI releases datasets publicly, fostering community advancements.
- An AMA was scheduled to discuss Olmo 3 and Molmo 2.
- The model's benchmarks are impressive for its size.

**Discussion Highlights:** The community is highly impressed by Molmo 2's capabilities, particularly its video analysis features and the public availability of datasets. There is excitement about the scheduled AMA and the model's performance benchmarks.

---

## 23. [XiaomiMiMo/MiMo-V2-Flash · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1po3bn4/xiaomimimomimov2flash_hugging_face/)

**Author:** u/Dark_Fire_12 | **Upvotes:** 239 | **Comments:** 52 | **Date:** 2025-12-16

**Summary:** The Reddit post discusses MiMo-V2-Flash, a Mixture-of-Experts (MoE) language model with 309B total parameters and 15B active parameters, designed for high-speed reasoning and agentic workflows. Users highlight its impressive performance on multilingual SWE tasks and inquire about larger versions and hardware requirements.

**Key Points:**
- MiMo-V2-Flash is a MoE language model with 309B total parameters and 15B active parameters.
- It shows strong performance on multilingual SWE tasks, surpassing models like Sonnet 4.5 and Gemini 3.
- Users discuss hardware requirements for running the model, such as using RTX 5060 Ti GPUs and 128 GB of RAM.
- There is interest in larger versions of the model.
- The tech report and blog links are provided for further details.

**Discussion Highlights:** Users express excitement about the model's performance and availability of weights. There is some skepticism about the performance claims, and discussions focus on hardware requirements and potential larger versions of the model.

---

## 24. [GLM-4.5V, GLM-4.6V and GLM_4.6V-Flash are now supported by llama.cpp (GGUFs)](https://reddit.com/r/LocalLLaMA/comments/1po18y9/glm45v_glm46v_and_glm_46vflash_are_now_supported/)

**Author:** u/jacek2023 | **Upvotes:** 170 | **Comments:** 34 | **Date:** 2025-12-16

**Summary:** The post announces that GLM-4.5V, GLM-4.6V, and GLM_4.6V-Flash models are now supported by llama.cpp with GGUFs, which is seen as a significant update by the community.

**Key Points:**
- Support for GLM-4.5V, GLM-4.6V, and GLM_4.6V-Flash has been added to llama.cpp.
- The update is celebrated as a great Christmas gift by the community.
- There is a question about whether GGUFs now support vision, as some repos state vision is not supported.
- A user mentions spending time setting up the new models.
- A comparison between Qwen3-VL-4B and GLM_4.6V is requested.

**Discussion Highlights:** The community is excited about the new model support, though there are questions about vision capabilities and comparisons with other models like Qwen3-VL-4B.

---

## 25. [Qwen3 Next speed optimization has been merged into llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1pnz9xu/qwen3_next_speed_optimization_has_been_merged/)

**Author:** u/jacek2023 | **Upvotes:** 215 | **Comments:** 25 | **Date:** 2025-12-16

**Summary:** The Reddit post discusses the recent speed optimization for Qwen3 Next in llama.cpp, highlighting significant performance improvements across different hardware configurations.

**Key Points:**
- Speed optimization for Qwen3 Next has been merged into llama.cpp
- Performance on M1 64GB improved from 12 t/s to 18 t/s
- Qwen3-30B achieves around 58 t/s on the same hardware
- Win11 + RTX5090 + vulkan setup achieves 37.x t/s without CUDA
- 100+ t/s possible with UD-Q2_K_XL without CPU offloading

**Discussion Highlights:** Users report significant performance gains, with notable improvements on various hardware setups, indicating a successful optimization effort.

---

## 26. [I may have over-quantized this little guy.](https://reddit.com/r/LocalLLaMA/comments/1pnz80z/i_may_have_overquantized_this_little_guy/)

**Author:** u/AllergicToTeeth | **Upvotes:** 137 | **Comments:** 33 | **Date:** 2025-12-16

**Summary:** The Reddit post humorously discusses the potential over-quantization of a model, with comments playfully referencing OpenAI, system prompts, and future GPT versions.

**Key Points:**
- Author may have over-quantized a model
- Comments reference OpenAI and system prompts
- Discussion includes humor about GPT-5.4 and GPT-5.3
- Mentions of quantization levels like Q0

**Discussion Highlights:** The discussion is lighthearted, with playful references to OpenAI and future GPT versions, indicating a community engaged in model development and quantization techniques.

---

## 27. [It was Ilya who "closed" OpenAI](https://reddit.com/r/LocalLLaMA/comments/1pnxekt/it_was_ilya_who_closed_openai/)

**Author:** u/licuphand | **Upvotes:** 512 | **Comments:** 234 | **Date:** 2025-12-16

**Summary:** The Reddit post discusses Ilya's role in 'closing' OpenAI, sparking a debate on trust in AI development and leadership dynamics among key figures like Elon, Ilya, and Sam.

**Key Points:**
- Ilya's actions are seen as pivotal in the direction of OpenAI.
- Trust in AI development is questioned, with skepticism about corporate control.
- Historical context of oversight is referenced, highlighting long-standing concerns.
- Leadership struggles among Elon, Ilya, and Sam are central to the discussion.
- The term 'CloseAI' is used to describe the trend of AI organizations becoming more closed.

**Discussion Highlights:** The discussion highlights a consensus that trust in AI development is fragile, with concerns about corporate control and leadership dynamics. Historical references to oversight and the term 'CloseAI' underscore the community's skepticism about the future of AI governance.

---

## 28. [Alibaba Open-Sources CosyVoice 3, a New TTS Model](https://reddit.com/r/LocalLLaMA/comments/1pnusp9/alibaba_opensources_cosyvoice_3_a_new_tts_model/)

**Author:** u/nekofneko | **Upvotes:** 220 | **Comments:** 31 | **Date:** 2025-12-16

**Summary:** Alibaba has open-sourced CosyVoice 3, a new TTS model with advanced features like multi-lingual support, high naturalness, and low latency. The model supports various instructions and text normalization, making it suitable for production use.

**Key Points:**
- Supports 9 languages and 18+ Chinese dialects with zero-shot voice cloning
- Achieves state-of-the-art performance in consistency, similarity, and naturalness
- Offers low latency (150ms) with bi-streaming support
- Supports pronunciation inpainting and text normalization
- Community discussion compares it favorably to other models like Chatterbox and Microsoft VibeVoice

**Discussion Highlights:** Users are excited about the release, comparing it to other TTS models like Chatterbox and Microsoft VibeVoice. There is interest in larger model versions and real-time voice cloning capabilities.

---

## 29. [New budget local AI rig](https://reddit.com/r/LocalLLaMA/comments/1pnllux/new_budget_local_ai_rig/)

**Author:** u/vucamille | **Upvotes:** 155 | **Comments:** 38 | **Date:** 2025-12-15

**Summary:** The user built a budget local AI rig using a Qiyida X99 motherboard, Xeon E5 2680 V4 CPU, 32GB RAM, and two MI50 16GB GPUs for around $650. The setup works well with ROCm 7.0.2 and can handle basic inference tasks, with plans for future upgrades.

**Key Points:**
- The total cost of the build was approximately $650, with the PSU being the most expensive component.
- The system uses dual MI50 16GB GPUs, which provide a 32GB VRAM pool and are expandable.
- ROCm 7.0.2 is functional, though the latest ROCm release had issues with multi-GPU support.
- The community praised the build for its affordability and performance, with some requesting benchmarks.
- The user plans to add brackets to prevent GPU sag and possibly more decorations.

**Discussion Highlights:** The community consensus was highly positive, with users praising the cost-effectiveness and performance of the build. Some users requested benchmarks, and there was general excitement about the potential for multi-GPU setups and future upgrades.

---

## 30. [I'm strong enough to admit that this bugs the hell out of me](https://reddit.com/r/LocalLLaMA/comments/1pnfaqo/im_strong_enough_to_admit_that_this_bugs_the_hell/)

**Author:** u/ForsookComparison | **Upvotes:** 1712 | **Comments:** 358 | **Date:** 2025-12-15

**Summary:** The Reddit post titled 'I'm strong enough to admit that this bugs the hell out of me' by u/ForsookComparison has gained significant attention with 1712 upvotes and 358 comments. The post appears to be a link post without text content, sparking a variety of humorous and technical responses from the community.

**Key Points:**
- The post has gained significant attention with 1712 upvotes and 358 comments
- The post is a link post without text content
- The top comments include humorous and technical responses
- One comment mentions downloading RAM Doubler to increase RAM
- Another comment discusses the performance of Mac Mini M4 Pro 64GB

**Discussion Highlights:** The discussion highlights include humorous suggestions like downloading RAM Doubler to increase RAM and technical comments about the performance of Mac Mini M4 Pro 64GB. The community seems engaged and responsive to the post, with a mix of light-hearted and serious contributions.

---

## 31. [They're finally here (Radeon 9700)](https://reddit.com/r/LocalLLaMA/comments/1pnd5uf/theyre_finally_here_radeon_9700/)

**Author:** u/Zeikos | **Upvotes:** 358 | **Comments:** 67 | **Date:** 2025-12-15

**Summary:** The post announces the arrival of Radeon 9700 GPUs, sparking community interest and requests for benchmarks. Users express nostalgia about the historic GPU name and enthusiasm for testing the new hardware.

**Key Points:**
- Community eagerly awaiting benchmarks for Radeon 9700
- Nostalgia expressed over the historic Radeon 9700 name
- Requests for inference, training, noise, and heat benchmarks
- Users planning to test the GPUs during holidays
- Jokes about hardware longevity and performance expectations

**Discussion Highlights:** The discussion is dominated by enthusiasm for benchmarking the new GPUs, with specific requests for performance metrics in inference and training tasks. There's a mix of nostalgia for the classic Radeon 9700 and humorous comments about hardware testing. The community appears eager to contribute testing data and share results.

---

## 32. [status of Nemotron 3 Nano support in llama.cpp](https://reddit.com/r/LocalLLaMA/comments/1pnc045/status_of_nemotron_3_nano_support_in_llamacpp/)

**Author:** u/jacek2023 | **Upvotes:** 180 | **Comments:** 32 | **Date:** 2025-12-15

**Summary:** The Reddit post discusses the status of Nemotron 3 Nano support in llama.cpp, highlighting a GitHub pull request and community reactions. Users appreciate Nvidia's approach and emphasize the importance of collaboration with llama.cpp for new model architectures.

**Key Points:**
- Nemotron 3 Nano support is being added to llama.cpp via a GitHub pull request.
- Community praises Nvidia's collaboration with llama.cpp as a model for other labs.
- Discussion includes technical details about model sizes and RAM/VRAM requirements.
- Users highlight the popularity and importance of llama.cpp in the AI community.

**Discussion Highlights:** The discussion consensus emphasizes the importance of collaboration between model developers and llama.cpp, with users praising Nvidia's approach and encouraging other labs to follow suit. Technical details about model sizes and requirements are also discussed.

---

## 33. [NVIDIA releases Nemotron 3 Nano, a new 30B hybrid reasoning model!](https://reddit.com/r/LocalLLaMA/comments/1pn8upp/nvidia_releases_nemotron_3_nano_a_new_30b_hybrid/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 836 | **Comments:** 178 | **Date:** 2025-12-15

**Summary:** NVIDIA has released Nemotron 3 Nano, a 30B hybrid reasoning model with a 1M context window and top performance in SWE-Bench, reasoning, and chat tasks. The model is available in GGUF format and is noted for its speed and efficiency.

**Key Points:**
- Nemotron 3 Nano is a 30B hybrid reasoning model
- Features a 1M context window
- Excels in SWE-Bench, reasoning, and chat performance
- Available in GGUF format
- Noted for high speed (110 t/s)

**Discussion Highlights:** The community discussion highlights the model's speed, its classification as part of the Nemotron 3 family of MoE models, and reactions to the 'nano' designation for a 30B model.

---

## 34. [NVIDIA Nemotron 3 Nano 30B A3B released](https://reddit.com/r/LocalLLaMA/comments/1pn8h5h/nvidia_nemotron_3_nano_30b_a3b_released/)

**Author:** u/rerri | **Upvotes:** 278 | **Comments:** 86 | **Date:** 2025-12-15

**Summary:** NVIDIA has released Nemotron 3 Nano 30B A3B, a new AI model featuring a hybrid Mamba-Transformer architecture, exceptional inference efficiency, and a 1M-token context window. The model is fully open-source and designed for high throughput and low latency.

**Key Points:**
- Hybrid Mamba-Transformer MoE architecture for efficient inference
- 31.6B total parameters with ~3.6B active per token
- Up to 4x faster than Nemotron Nano 2 and leading models in its size category
- 1M-token context window for long-horizon workflows
- Fully open with open weights, datasets, and training recipes

**Discussion Highlights:** The discussion highlights include a Llama.cpp PR for integration, questions about optimal Unsloth quant settings for specific hardware, concerns about synthetic data training, and performance feedback from users who have tested the model.

---

## 35. [How to do a RTX Pro 6000 build right](https://reddit.com/r/LocalLLaMA/comments/1pn6ijr/how_to_do_a_rtx_pro_6000_build_right/)

**Author:** u/GPTrack_dot_ai | **Upvotes:** 118 | **Comments:** 174 | **Date:** 2025-12-15

**Summary:** The post discusses building a high-performance system using 8x Nvidia RTX Pro 6000 GPUs with integrated 400G networking, emphasizing ease of setup with the right CPU, RAM, and storage. The system is described as ready-to-use with minimal configuration needed.

**Key Points:**
- RTX Pro 6000 GPUs lack NVlink but feature integrated 400G networking for high-speed connectivity.
- The system requires careful selection of CPU, RAM, and storage to complement the GPUs.
- The build is described as straightforward with minimal risk of errors.
- Users expressed awe at the system's specifications and cost.
- The system is heavy (70 kg) and requires robust power supply (6000W TDP).

**Discussion Highlights:** Users were impressed by the system's specifications, comparing it to luxury items like Ferraris and private jets. There was humor about the cost and a general consensus on the system's high performance and complexity.

---

## 36. [New Google model incoming!!!](https://reddit.com/r/LocalLLaMA/comments/1pn37mw/new_google_model_incoming/)

**Author:** u/R46H4V | **Upvotes:** 1259 | **Comments:** 263 | **Date:** 2025-12-15

**Summary:** The Reddit post discusses anticipation and speculation around an upcoming new Google model, with links to relevant sources. The community expresses hope for significant improvements and multi-modal capabilities.

**Key Points:**
- Anticipation of a new Google model
- Hope for improvements over previous models like Gemma3-Math
- Speculation about multi-modal capabilities
- Community excitement and hype
- Mention of potential models like Gemma 4

**Discussion Highlights:** The discussion highlights a strong sense of anticipation and hope within the community for a significant advancement in Google's model capabilities, particularly in multi-modal features. There is also a consensus of excitement and speculation about what the new model might offer.

---

## 37. [llama.cpp: Automation for GPU layers, tensor split, tensor overrides, and context size (with MoE optimizations)](https://reddit.com/r/LocalLLaMA/comments/1pn2e1c/llamacpp_automation_for_gpu_layers_tensor_split/)

**Author:** u/Remove_Ayys | **Upvotes:** 188 | **Comments:** 62 | **Date:** 2025-12-15

**Summary:** The post discusses a new feature in llama.cpp that automates memory allocation across GPUs, improving usability and performance for hybrid CPU+GPU inference. The implementation uses virtual test allocations to iteratively adjust memory use, prioritizing dense tensors for better MoE performance.

**Key Points:**
- Automation of memory allocation for GPU layers and tensor splits in llama.cpp
- Virtual test allocations used to iteratively reduce memory use
- Dense tensors prioritized for better MoE performance
- Implementation is generic and works with any ggml backend supporting hybrid inference
- Potential for caching to eliminate fitting time in future updates

**Discussion Highlights:** The community appreciates the new feature, with suggestions for further improvements like caching and special handling for dense models. Users also express interest in multi-GPU setups and more efficient memory management.

---

## 38. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 935 | **Comments:** 210 | **Date:** 2025-12-14

**Summary:** The Reddit post titled 'Aaaand... is gone...' in r/LocalLLaMA discusses the discontinuation or scarcity of a technology, likely SATA drives, sparking a conversation about storage solutions and their implications.

**Key Points:**
- The post is a link with no text content, focusing on the title and comments for context.
- One user mentions buying a 2TB SSD, indicating a shift towards alternative storage solutions.
- A comment references a GIF, possibly illustrating the topic humorously or visually.
- Another comment suggests the post is about SATA drives, downplaying its significance as a 'nothingburger'.
- The discussion highlights differing opinions on the impact of the topic, with some seeing it as a major issue and others as insignificant.

**Discussion Highlights:** The discussion revolves around the implications of the post's topic, with users sharing their perspectives on storage technology and its future. Some users see the topic as a significant issue, while others downplay its importance, creating a balanced debate.

---

## 39. [Qwen3-Next-80B-A3B-Thinking-GGUF has just been released on HuggingFace](https://reddit.com/r/LocalLLaMA/comments/1pmo0dn/qwen3next80ba3bthinkinggguf_has_just_been/)

**Author:** u/LegacyRemaster | **Upvotes:** 124 | **Comments:** 54 | **Date:** 2025-12-14

**Summary:** The Reddit post announces the release of Qwen3-Next-80B-A3B-Thinking-GGUF on HuggingFace, highlighting its impressive performance in a Tetris game implemented in a single HTML file. The model is praised for its accuracy and potential for agentic coding tasks.

**Key Points:**
- Qwen3-Next-80B-A3B-Thinking-GGUF model released on HuggingFace
- Model excels in Tetris game implementation in a single HTML file
- Performance compared favorably to Devstral
- Community impressed by its capabilities for iterative agentic coding
- Discussion includes questions about release timing and training data

**Discussion Highlights:** The community is highly impressed with the model's performance, with some users noting its potential for agentic coding tasks. There are discussions about the release timing, training data inclusion, and compatibility with tools like llamacpp.

---

## 40. [To Mistral and other lab employees: please test with community tools BEFORE releasing models](https://reddit.com/r/LocalLLaMA/comments/1pmgm2x/to_mistral_and_other_lab_employees_please_test/)

**Author:** u/dtdisapointingresult | **Upvotes:** 135 | **Comments:** 72 | **Date:** 2025-12-14

**Summary:** The Reddit post criticizes Mistral for releasing Devstral 2 without thorough testing with community tools, leading to issues like benchmark discrepancies and repetition loops. The author emphasizes the importance of testing with local tools to maintain reputation and user trust. Key points include the lack of testing with community tools, issues with benchmark discrepancies and repetition loops, and the importance of tech geeks' recommendations. The discussion highlights mixed experiences with the model and a consensus on the need for thorough testing with community tools before release.

---

## 41. [Understanding the new router mode in llama cpp server](https://reddit.com/r/LocalLLaMA/comments/1pmc7lk/understanding_the_new_router_mode_in_llama_cpp/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 172 | **Comments:** 44 | **Date:** 2025-12-14

**Summary:** Router mode in llama cpp server allows managing multiple AI models simultaneously without restarting the server, similar to Ollama's functionality. It enables loading/unloading models on demand and routing requests to the appropriate model, saving memory and simplifying model switching.

**Key Points:**
- Router mode enables managing multiple AI models in a single server process.
- It allows loading/unloading models on demand and routing requests to the correct model.
- This feature saves memory and simplifies switching between models.
- Useful for testing multiple GGUF models, building local OpenAI-compatible APIs, and dynamic model switching.
- Discussion highlights include comparisons with llama-swap and requests for better VRAM management.

**Discussion Highlights:** The discussion includes comparisons with llama-swap, with users noting similarities and differences. There are requests for better VRAM management, especially for users with multiple GPUs. Some users express interest in specifying which models stay in memory concurrently.

---

## 42. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 629 | **Comments:** 268 | **Date:** 2025-12-13

**Summary:** The user detailed their journey of upgrading a GPU server, culminating in a setup with 8x RTX Pro 6000 GPUs, a Threadripper PRO 9955WX CPU, and 384 GB RAM, totaling 768 GB VRAM. They faced challenges with heat management, power consumption, and hardware compatibility, ultimately resolving issues with a larger case and a server-grade platform.

**Key Points:**
- The server features 8x RTX Pro 6000 GPUs (4 Workstation, 4 Max-Q), a Threadripper PRO 9955WX CPU, and 384 GB RAM, providing 768 GB VRAM.
- The user faced heat issues with earlier setups, leading to system crashes and the need for better cooling solutions.
- Hardware compatibility issues arose with consumer-grade motherboards, prompting a switch to a server-grade platform.
- Power consumption was a significant challenge, requiring separate breakers for the GPUs.
- The community discussion highlighted concerns about the setup's physical stability and cooling solutions.

**Discussion Highlights:** The discussion included praise for the impressive hardware setup, concerns about the physical stability and cooling of the system, and anecdotes about power supply issues. The top comment humorously compared the setup to a 'Porsche in a trailer park,' emphasizing the contrast between high-end components and the makeshift cooling solution.

---

## 43. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 170 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that they share nearly identical sizes and architectures, with minor differences in expert configurations. The author highlights the open-source nature of these models and mentions that Mistral 3 likely trained its model from scratch despite architectural similarities.

**Key Points:**
- Mistral 3 Large and DeepSeek V3 have nearly identical sizes (671B vs. 673B) and share the same architecture.
- Mistral 3 adjusted the expert configuration by increasing expert size while decreasing their number, aiming to improve latency.
- Mistral 3 is likely trained from scratch rather than fine-tuned from DeepSeek V3, as it uses its own tokenizer.
- The DeepSeek V3 architecture is being adopted by multiple models, including Kimi K2 and Gigachat, showcasing open-source collaboration.
- The community discussion highlights the effectiveness and efficiency of the DeepSeek V3 architecture, with some noting its suitability for resource-constrained environments.

**Discussion Highlights:** The discussion emphasizes the open-source spirit, with multiple models adopting the DeepSeek V3 architecture. Users appreciate the innovation and efficiency of the architecture, while also noting Mistral's additional work on multimodal capabilities. There is consensus on the effectiveness of the DeepSeek V3 architecture for large-scale models.

---

## 44. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 621 | **Comments:** 112 | **Date:** 2025-12-13

**Summary:** OpenAI's ChatGPT-5.2 model is ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and processing clinical notes for QA evaluation.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report the model performs poorly on follow-up questions and research tasks compared to previous versions.
- The model frequently denies processing made-up clinical notes for QA evaluation, which was not an issue with earlier models.
- Questions about the testing criteria for the Sansa benchmark, especially regarding Grok's low ranking.
- Observations that Gemini is less censored than other models, including Mistral.

**Discussion Highlights:** Users express dissatisfaction with ChatGPT-5.2's performance and censorship levels, noting declines in functionality and comparing it unfavorably to other AI models like Gemini and Mistral.

---

## 45. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 364 | **Comments:** 40 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations for Qwen3, specifically an optimized autoregressive delta net computation that results in a 40% generation speed upgrade. The author invites community feedback on the implementation.

**Key Points:**
- Optimized autoregressive delta net computation implemented
- 40% generation speed upgrade reported
- Community invited to test and provide feedback
- Positive community reaction with high upvotes on comments
- Inquiry about compatibility with ROCm/Vulkan platforms

**Discussion Highlights:** The community responded positively to the optimization, with comments highlighting the author's frequent contributions and expressing interest in further improvements. There was also a question about the speedup's compatibility with non-CUDA platforms like ROCm and Vulkan.

---

## 46. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 244 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve text generation throughput using Eagle3 speculative decoding. It is licensed for both commercial and non-commercial use in various AI applications.

**Key Points:**
- GPT-OSS-120B-Eagle3-throughput is an optimized speculative decoding module built on OpenAI's gpt-oss-120b base model.
- It uses NVIDIA’s Eagle3 speculative decoding approach to predict a single draft token efficiently.
- The model is licensed under the nvidia-open-model-license for commercial and non-commercial use.
- It is intended for applications like AI agents, chatbots, and retrieval-augmented generation (RAG) systems.
- The model is not supported in llama.cpp, as indicated in the discussion.

**Discussion Highlights:** The discussion includes inquiries about making the model derestricted, its potential benefits for CPU inference, and the lack of support in llama.cpp. There is also a humorous comment about waiting for a REAP EAGLE3 HERETIC MOE GGUF version.

---

## 47. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 238 | **Comments:** 77 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which is seen as a decline in their approach. Key points include the criticism of OpenAI's focus on normies rather than programmers, the irony of their shift from warning about open models to using astrology ads, and the consensus that this strategy might be more profitable but is seen as a fall from grace. The discussion highlights a consensus that OpenAI's shift in advertising strategy is seen as a decline in their approach, with some suggesting alternative strategies like leveraging user data.

---

## 48. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 297 | **Comments:** 35 | **Date:** 2025-12-12

**Summary:** The Reddit post discusses the feasibility and novelty of running an LLM on a 3DS, drawing comparisons to similar projects on other platforms like the PS Vita and Wii. The community expresses admiration for the technical achievement and speculates about performance improvements on newer hardware.

**Key Points:**
- Running an LLM on a 3DS is a notable technical achievement.
- Comparisons are made to similar projects on the PS Vita and Wii.
- The community is impressed by the project's novelty.
- Discussions include potential performance improvements on newer hardware like the 'new' 3DS.

**Discussion Highlights:** The discussion highlights the community's admiration for the technical feat of running an LLM on a 3DS, with comparisons to other platforms and speculation about performance improvements on updated hardware.

---

## 49. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 593 | **Comments:** 125 | **Date:** 2025-12-12

**Summary:** The user shares their upgraded 'Monster-server' setup, featuring a Ryzen 3950x CPU, three GPUs (2x RTX 3090 and 1x RTX 4090), and extensive storage. They use it to run local LLMs like GPT-OSS-120B for research and coding, expressing satisfaction with the performance and cost-effectiveness of the build.

**Key Points:**
- The server uses a Ryzen 3950x CPU and three GPUs, including an RTX 4090, for running local LLMs.
- The setup includes 128GB RAM, 8TB NVMe storage, and 72TB HDD storage for virtualized TrueNAS.
- The user runs GPT-OSS-120B fully in VRAM, achieving over 100 tokens per second.
- A notable comment mentions that a 3-GPU setup is slower compared to 2 or 4 GPU setups due to Tensor Parallel vs. Pipeline Parallel.
- The user has 10GB fiber internet for $50/month, sparking interest in their location.

**Discussion Highlights:** The discussion highlights nostalgia for early 2000s overclocking forums, curiosity about the user's location due to affordable high-speed internet, and technical insights about GPU setups and their impact on performance. Some users expressed envy and admiration for the build.

---

## 50. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 179 | **Comments:** 28 | **Date:** 2025-12-12

**Summary:** The post introduces Olmo 3.1 32B Think and Instruct models, two new 32-billion-parameter models in the Olmo family, each optimized for different use cases. The Think model specializes in deep reasoning, while the Instruct model focuses on instruction following and conversational fluency. The community response is positive, highlighting the models' open-source nature and continuous improvement.

**Key Points:**
- Olmo 3.1 32B Think and Instruct models are the newest additions to the Olmo family.
- The Think model is optimized for deep reasoning, math, logic, and code generation.
- The Instruct model is designed for instruction following, conversational fluency, and tool-use capabilities.
- The models are fully open-source and praised for their quality and improvement.
- Community expectations include potential future developments like MOE (Mixture of Experts).

**Discussion Highlights:** The discussion highlights a positive reception of the new models, with users appreciating their open-source nature and the educational value of the accompanying paper. There is also anticipation for future advancements, such as the potential introduction of Mixture of Experts (MOE) models.

---

