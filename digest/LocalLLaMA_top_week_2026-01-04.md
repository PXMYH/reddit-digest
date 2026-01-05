# r/LocalLLaMA Reading Digest

**Period:** 2026-01-04 to 2026-01-04
**Posts Summarized:** 34
**Total Posts Analyzed:** 34

---

## 1. [MultiverseComputingCAI/HyperNova-60B · Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1q3p9oz/multiversecomputingcaihypernova60b_hugging_face/)

**Author:** u/jacek2023 | **Upvotes:** 114 | **Comments:** 57 | **Date:** 2026-01-04

**Summary:** The Reddit post discusses HyperNova 60B, a model based on the gpt-oss-120b architecture with 59B parameters, 4.8B active parameters, and MXFP4 quantization. It supports configurable reasoning effort and requires less than 40GB of GPU memory. The discussion highlights its novel compression technology and user experiences with the model.

**Key Points:**
- HyperNova 60B is based on the gpt-oss-120b architecture
- It has 59B parameters with 4.8B active parameters and uses MXFP4 quantization
- The model supports configurable reasoning effort (low, medium, high)
- It requires less than 40GB of GPU memory
- The discussion highlights its novel compression technology and user experiences

**Discussion Highlights:** Users discussed the novel compression technology used in HyperNova 60B and shared their experiences with the model, including its performance on different hardware configurations.

---

## 2. [Local LLMs vs breaking news: when extreme reality gets flagged as a hoax - the US/Venezuela event was too far-fetched](https://reddit.com/r/LocalLLaMA/comments/1q31ltd/local_llms_vs_breaking_news_when_extreme_reality/)

**Author:** u/ubrtnk | **Upvotes:** 351 | **Comments:** 186 | **Date:** 2026-01-03

**Summary:** The post discusses how local LLMs struggled to accept the breaking news of the US attacking Venezuela and capturing Maduro, with models like Qwen Research and Spark initially classifying the event as a hoax despite credible sources. The user had to adjust prompts and provide multiple sources to get the models to acknowledge the event's reality.

**Key Points:**
- Local LLMs initially dismissed the US/Venezuela event as a hoax despite credible sources.
- Models like Qwen Research and Spark required extensive prompting and evidence to accept the news.
- Larger models (e.g., GPT-OSS:120B) handled verification more efficiently than smaller ones.
- Community comments highlight similar issues with LLMs dismissing extreme or unfamiliar events.
- Discussion suggests LLMs may have inherent biases in interpreting geopolitical events.

**Discussion Highlights:** The community consensus reflects frustration with LLMs' tendency to dismiss extreme or unfamiliar events as misinformation, even when provided with credible sources. Users noted similar experiences with other unlikely events, indicating a broader issue with LLM skepticism toward breaking news.

---

## 3. [Llama.cpp running on Android with Snapdragon 888 and 8GB of ram. Compiled/Built on device. [Guide/Tutorial]](https://reddit.com/r/LocalLLaMA/comments/1q2wvsj/llamacpp_running_on_android_with_snapdragon_888/)

**Author:** u/hackiv | **Upvotes:** 124 | **Comments:** 35 | **Date:** 2026-01-03

**Summary:** The post provides a guide on running Llama.cpp on Android devices with Snapdragon 888 and 8GB RAM, detailing steps from downloading Termux to launching the server and accessing it via a web browser. The discussion highlights alternative installation methods and performance considerations for different model quantizations.

**Key Points:**
- Guide to compile and run Llama.cpp on Android using Termux
- Steps include downloading Termux, cloning the repository, building with CMake, and launching the server
- Model is saved in cache for future use without re-downloading
- Alternative installation method via Termux package mentioned in comments
- Performance considerations for different model quantizations (Q4_K_M vs Q4_0)

**Discussion Highlights:** The discussion highlights an alternative installation method using the Termux package 'llama-cpp' and performance considerations for different model quantizations, with Q4_0 being recommended for faster performance on ARM devices. There is also a mention of the importance of on-device compilation for ARM optimizations.

---

## 4. [ElevenLabs is killing my budget. What are the best "hidden gem" alternatives for documentary style TTS?](https://reddit.com/r/LocalLLaMA/comments/1q2sfwx/elevenlabs_is_killing_my_budget_what_are_the_best/)

**Author:** u/Ancient_Routine8576 | **Upvotes:** 211 | **Comments:** 98 | **Date:** 2026-01-03

**Summary:** The post discusses alternatives to ElevenLabs for documentary-style TTS, focusing on cost-effective and local solutions with a dark, authoritative tone. Users recommend tools like Soprano, Kokoro, VibeVoice, XTTS v2, and F5 TTS.

**Key Points:**
- Author seeks cost-effective alternatives to ElevenLabs for long-form content.
- Prefer tools with a dark, authoritative, documentary-style tone.
- Local solutions like Soprano, Kokoro, VibeVoice, XTTS v2, and F5 TTS are recommended.
- VibeVoice is highlighted for ease of use without coding.
- Echo-TTS is mentioned but has a 30-second limitation.

**Discussion Highlights:** The discussion highlights several local TTS tools as viable alternatives, with VibeVoice being noted for its ease of use and high-quality output. Some users mention instability in certain models but overall consensus points towards these tools as cost-effective solutions.

---

## 5. [Don't sleep on granite 4 small if you got an 8+32+ system](https://reddit.com/r/LocalLLaMA/comments/1q2s3hp/dont_sleep_on_granite_4_small_if_you_got_an_832/)

**Author:** u/Zestyclose-Shift710 | **Upvotes:** 110 | **Comments:** 46 | **Date:** 2026-01-03

**Summary:** The post discusses optimizing a ThinkPad P15 with 32GB RAM and an 8GB Quadro GPU to run large language models efficiently. By using a Mixture of Experts (MoE) model and keeping experts in CPU, the user achieved high context lengths and usable generation speeds, particularly with the Granite 4.0 Small model.

**Key Points:**
- Using a MoE model and keeping experts in CPU frees up VRAM for larger context lengths.
- Granite 4.0 Small (32B total / 9B activated) maintains speed even with large context lengths.
- Achieved ~7 tokens per second with a 50-page (~50.5k tokens) paper in context.
- Comparison with Qwen 30B A3B and other models discussed in comments.
- Potential improvements and issues with Vulkan inference mentioned.

**Discussion Highlights:** The discussion highlights comparisons with other models like Qwen 30B A3B, potential speed improvements using specific parameters, and ongoing issues with Vulkan inference that need addressing.

---

## 6. [GLM-4.7-REAP-50-W4A16: 50% Expert-Pruned + INT4 Quantized GLM-4 (179B params, ~92GB)](https://reddit.com/r/LocalLLaMA/comments/1q2pons/glm47reap50w4a16_50_expertpruned_int4_quantized/)

**Author:** u/Maxious | **Upvotes:** 174 | **Comments:** 70 | **Date:** 2026-01-03

**Summary:** The post introduces GLM-4.7-REAP-50-W4A16, a 50% expert-pruned and INT4 quantized version of GLM-4 with 179B parameters (~92GB). The discussion focuses on technical details like calibration methods, benchmarking, and comparisons with other models.

**Key Points:**
- GLM-4.7-REAP-50-W4A16 is a pruned and quantized version of GLM-4 with 179B parameters (~92GB).
- Community members request details on calibration methods for expert activation during quantization.
- Questions arise about the tasks used for REAP pruning calibration.
- Interest in benchmark results and comparisons with models like MiniMax M2.1.
- Subjective comparisons with EXL3 GLM suggest potential performance differences.

**Discussion Highlights:** The discussion highlights a strong interest in technical details such as calibration processes and benchmarking. Some users express preferences for alternative models based on subjective performance evaluations, while others await formal benchmark results.

---

## 7. [What is the smartest uncensored nsfw LLM you can run with 20GB VRAM and 24GB RAM](https://reddit.com/r/LocalLLaMA/comments/1q2o033/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Death_12_35_taken | **Upvotes:** 180 | **Comments:** 74 | **Date:** 2026-01-03

**Summary:** The post seeks recommendations for an uncensored, smart, and fast LLM that can run locally with 20GB VRAM and 24GB RAM. Users suggest models like Dolphin-Mistral-24B-Venice-Edition and others from the UGI-Leaderboard.

**Key Points:**
- User seeks an uncensored, smart, and fast LLM for local use with specific hardware constraints.
- Dolphin-Mistral-24B-Venice-Edition is recommended for its performance and features.
- UGI-Leaderboard provides a list of potential models suitable for the user's requirements.
- Additional models like Huihui-Qwen3-VL-30B-A3B-Instruct-abliterated are mentioned as alternatives.

**Discussion Highlights:** The discussion highlights a consensus around the Dolphin-Mistral-24B-Venice-Edition model for its balance of performance and uncensored capabilities. Users also point to the UGI-Leaderboard for a broader selection of models that fit the hardware constraints.

---

## 8. [How is Cloud Inference so cheap](https://reddit.com/r/LocalLLaMA/comments/1q2jwsn/how_is_cloud_inference_so_cheap/)

**Author:** u/VolkoTheWorst | **Upvotes:** 100 | **Comments:** 102 | **Date:** 2026-01-02

**Summary:** The Reddit post discusses how cloud inference companies manage to offer services at low prices despite high GPU and electricity costs. The discussion highlights strategies like batching, scaling, and quantization, but also questions the profitability of these companies. Key points include: Batching allows one GPU to serve hundreds of users simultaneously; many companies may not be profitable yet, relying on future projections; scale, batching, and quantization improve efficiency; some companies operate at a loss, hoping to outlast competitors; and efficiency gains come from horizontal scaling and model optimization. The discussion suggests that while batching and scaling improve efficiency, many cloud inference providers may not be profitable yet. There is a consensus that companies are operating at a loss, betting on future profitability or market dominance.

---

## 9. [LeCun Says Llama 4 results "were fudged a little bit"](https://reddit.com/r/LocalLLaMA/comments/1q25070/lecun_says_llama_4_results_were_fudged_a_little/)

**Author:** u/MrPecunius | **Upvotes:** 360 | **Comments:** 89 | **Date:** 2026-01-02

**Summary:** Yann LeCun, departing Meta AI Chief, confirmed that Llama 4 benchmark results were manipulated, leading to organizational changes at Meta. The community expressed disappointment and shared insights on the implications for open-source AI development.

**Key Points:**
- LeCun confirmed Llama 4 benchmark manipulation
- Zuckerberg sidelined the GenAI organization, leading to departures
- Community disappointment over Llama 4's lack of progress
- Discussion on the impact of Meta's decisions on open-source AI
- Shared link to the full article for further reading

**Discussion Highlights:** The community expressed disappointment over the lack of progress with Llama 4 and discussed the broader implications of Meta's decisions on open-source AI development. Notable comments included sharing the full article and questioning Meta's strategic decisions.

---

## 10. [Most optimal vram/performance per price and advice for Shenzhen GPU market](https://reddit.com/r/LocalLLaMA/comments/1q1w1qj/most_optimal_vramperformance_per_price_and_advice/)

**Author:** u/notafakename10 | **Upvotes:** 250 | **Comments:** 61 | **Date:** 2026-01-02

**Summary:** The post seeks advice on purchasing GPUs in Shenzhen with a budget of $1500-3000 USD, aiming for at least 48GB VRAM and good performance for local models and PyTorch training. The discussion highlights various GPU options and their pros and cons. Key points include the budget range, target VRAM, use case, options considered, and the importance of cooling and power requirements. The discussion suggests MI100 for best value if CUDA is not needed, and 4090D 48GB if CUDA is required. Other options like A100 and A40s are mentioned but may be out of budget. Cooling and power are emphasized as important considerations.

---

## 11. [Getting ready to train in Intel arc](https://reddit.com/r/LocalLLaMA/comments/1q1p5q5/getting_ready_to_train_in_intel_arc/)

**Author:** u/hasanismail_ | **Upvotes:** 298 | **Comments:** 91 | **Date:** 2026-01-01

**Summary:** A user is preparing to train on Intel Arc GPUs and shares their excitement, while also addressing concerns about GPU shortages. The community provides feedback and suggestions for setup.

**Key Points:**
- User is waiting for PCIe risers to start training on Intel Arc GPUs
- User clarifies they are not causing a GPU shortage
- Community suggests using Ubuntu 24.04 and mentions support for Intel Arc in Unsloth
- Recommendation to join OpenArc Discord for setup assistance
- Discussion about the feasibility of training on PCIe setup vs renting N*H100 from Vast

**Discussion Highlights:** The community is supportive and provides practical advice, such as using Ubuntu 24.04 and joining OpenArc Discord. There is also a discussion about the constraints of training on a PCIe setup compared to renting more powerful GPUs.

---

## 12. [TIL you can allocate 128 GB of unified memory to normal AMD iGPUs on Linux via GTT](https://reddit.com/r/LocalLLaMA/comments/1q1lgb7/til_you_can_allocate_128_gb_of_unified_memory_to/)

**Author:** u/1ncehost | **Upvotes:** 173 | **Comments:** 30 | **Date:** 2026-01-01

**Summary:** The post discusses using AMD's GTT feature on Linux to allocate up to 128 GB of system memory as VRAM for iGPUs, enabling parallel GPU tasks like kernel development while training models on the main GPU. Users share experiences with this feature for background tasks and hybrid CPU/GPU architectures.

**Key Points:**
- AMD iGPUs on Linux can use up to 128 GB of system memory as VRAM via GTT, dynamically allocated.
- Useful for development tasks like kernel profiling, but not ideal for inference due to iGPU slowness.
- Users report success with background LLM tasks and hybrid CPU/GPU setups.
- GTT allows parallel GPU tasks, such as training on the main GPU while optimizing kernels on the iGPU.
- Similar techniques can be applied to Nvidia GPUs for tasks like kv cache management.

**Discussion Highlights:** The discussion highlights practical applications of GTT for background tasks and hybrid architectures, with users sharing positive experiences. However, it's noted that iGPUs are generally slower than CPUs for inference tasks.

---

## 13. [IQuestCoder - new 40B dense coding model](https://reddit.com/r/LocalLLaMA/comments/1q1986x/iquestcoder_new_40b_dense_coding_model/)

**Author:** u/ilintar | **Upvotes:** 182 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The post introduces IQuestCoder, a new 40B dense coding model based on Llama architecture, adapted to GGUF format, with claims of SOTA performance. The discussion highlights positive feedback on its performance and questions about its architecture.

**Key Points:**
- IQuestCoder is a 40B dense coding model based on Llama architecture
- Adapted to GGUF format and works with Llama.cpp
- Claims of SOTA performance
- Positive feedback on performance in tasks like coding and game development
- Questions about the model's architecture and transparency

**Discussion Highlights:** The discussion highlights positive feedback on the model's performance, with users testing it in various coding tasks. However, there are questions about the model's architecture and transparency, with some users expressing skepticism.

---

## 14. [Upstage Solar-Open-100B Public Validation](https://reddit.com/r/LocalLLaMA/comments/1q0zst6/upstage_solaropen100b_public_validation/)

**Author:** u/PerPartes | **Upvotes:** 234 | **Comments:** 69 | **Date:** 2026-01-01

**Summary:** Upstage hosted an event at KAIST, Seoul, to counter claims that their Solar-Open-100B model is merely a fine-tuned version of GLM-Air-4.5. The event featured CEO Sung Kim and was live-streamed on YouTube. The post includes links to the LinkedIn announcement and the event video.

**Key Points:**
- Upstage's official response to plagiarism claims about Solar-Open-100B
- Event held at KAIST, Seoul, with CEO Sung Kim as presenter
- YouTube live stream available for the event
- Discussion includes technical tests and community reactions
- Mixed reactions with some users calling for broader accessibility

**Discussion Highlights:** The discussion includes technical analysis of model similarities, community reactions to the event's exclusivity, and debates about the necessity of in-person events versus online releases. Some users expressed skepticism about the claims, while others defended Upstage's integrity based on prior interactions.

---

## 15. [DeepSeek new paper: mHC: Manifold-Constrained Hyper-Connections](https://reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/)

**Author:** u/External_Mood4719 | **Upvotes:** 168 | **Comments:** 37 | **Date:** 2026-01-01

**Summary:** The Reddit post discusses DeepSeek's new paper on mHC (Manifold-Constrained Hyper-Connections), highlighting its significance in improving deep network architectures, particularly in LLMs and CNNs like ResNet. Key points include the introduction of mHC for gradient handling, the importance of residual connections, and optimism about future advancements. The discussion emphasizes the need for better gradient management and the potential impact of mHC.

---

## 16. [Software FP8 for GPUs without hardware support - 3x speedup on memory-bound operations](https://reddit.com/r/LocalLLaMA/comments/1q0x8ci/software_fp8_for_gpus_without_hardware_support_3x/)

**Author:** u/Venom1806 | **Upvotes:** 278 | **Comments:** 57 | **Date:** 2026-01-01

**Summary:** A user developed a software-based FP8 implementation for GPUs without native support, achieving a 3x speedup on memory-bound operations. The solution is compatible with older GPUs and is open for community feedback.

**Key Points:**
- Software-based FP8 implementation using bitwise operations and Triton kernels
- 3x speedup on memory-bound operations like GEMV and FlashAttention
- Compatible with RTX 30/20 series and older GPUs without native FP8 support
- Early stage but functional, with open-source availability
- Community interest in extending GPU lifespan and integration with tools like ComfyUI

**Discussion Highlights:** The community praised the workaround as a valuable hack, with discussions clarifying FP8 support on RTX 30 series and potential integrations. Some users shared their experiences with FP8 on their GPUs and expressed interest in further development.

---

## 17. [IQuestLab/IQuest-Coder-V1 — 40B parameter coding LLM — Achieves leading results on SWE-Bench Verified (81.4%), BigCodeBench (49.9%), LiveCodeBench v6 (81.1%)](https://reddit.com/r/LocalLLaMA/comments/1q0vom4/iquestlabiquestcoderv1_40b_parameter_coding_llm/)

**Author:** u/TellMeAboutGoodManga | **Upvotes:** 175 | **Comments:** 45 | **Date:** 2025-12-31

**Summary:** IQuestLab's IQuest-Coder-V1 is a 40B parameter coding LLM that achieves leading results on multiple benchmarks, including SWE-Bench Verified (81.4%), BigCodeBench (49.9%), and LiveCodeBench v6 (81.1%). The model is backed by a Chinese quant trading company, similar to DeepSeek, and has sparked discussions about its performance and architecture.

**Key Points:**
- 40B parameter dense model with top benchmark scores
- Backed by a Chinese quant trading company
- Community questions about benchmark validity and model architecture
- Not a Mixture of Experts (MoE) model despite its size
- Comparisons to other models like DeepSeek

**Discussion Highlights:** The community discussion includes skepticism about whether the benchmarks are genuine ('Benchmaxxed or real?'), observations about the model being a dense rather than MoE architecture, and comparisons to other models backed by quant trading firms. Some users also shared additional context about the company's background.

---

## 18. [Happy New Year: Llama3.3-8B-Instruct-Thinking-Claude-4.5-Opus-High-Reasoning - Fine Tune. (based on recent find of L3.3 8b in the wild)](https://reddit.com/r/LocalLLaMA/comments/1q0uuqt/happy_new_year/)

**Author:** u/Dangerous_Fix_5526 | **Upvotes:** 276 | **Comments:** 80 | **Date:** 2025-12-31

**Summary:** The post announces a fine-tuned Llama3.3-8B model using the Claude 4.5 Opus High Reasoning dataset, with GGUF quantizations now available. The author thanks contributors and provides links to the model and dataset. Key points include the fine-tuning process, the availability of GGUF quantizations, and the release of a Heretic (uncensored) version. The discussion highlights questions about the dataset size and interest in the GGUF version.

---

## 19. [Moonshot AI Completes $500 Million Series C Financing](https://reddit.com/r/LocalLLaMA/comments/1q0i4g3/moonshot_ai_completes_500_million_series_c/)

**Author:** u/InternationalAsk1490 | **Upvotes:** 110 | **Comments:** 21 | **Date:** 2025-12-31

**Summary:** Moonshot AI has completed a $500 million Series C financing, with plans to expand GPU capacity and develop the K3 model. The company aims to achieve significant revenue growth and enhance its model's capabilities.

**Key Points:**
- Moonshot AI completed a $500 million Series C financing.
- The company's global paid user base is growing at a monthly rate of 170%.
- Funds will be used to expand GPU capacity and accelerate the development of the K3 model.
- Key priorities for 2026 include improving the K3 model's performance and achieving significant revenue growth.
- The discussion highlights positive sentiment towards Moonshot AI's progress and its Kimi models.

**Discussion Highlights:** The discussion highlights positive sentiment towards Moonshot AI's progress, with users expressing satisfaction with the Kimi models and the company's financial achievements.

---

## 20. [Solar-Open-100B is out](https://reddit.com/r/LocalLLaMA/comments/1q0bgvl/solaropen100b_is_out/)

**Author:** u/cgs019283 | **Upvotes:** 156 | **Comments:** 62 | **Date:** 2025-12-31

**Summary:** Upstage has released the Solar-Open-100B model, a 102B parameter model with a commercial-friendly license. The community is excited about the rapid advancements in model quality and the potential for local inference.

**Key Points:**
- 102B parameter model with commercial license
- Community excitement about rapid model advancements
- Anticipation for performance benchmarks and quantized versions
- Mention of 19.7 trillion training tokens
- Speculation about model being GLM4.6-Air

**Discussion Highlights:** The community is highly positive about the release, noting the rapid pace of model improvements. There is anticipation for performance benchmarks and quantized versions for local use. Some users are speculating about the model's origins and training data.

---

## 21. [Qwen-Image-2512](https://reddit.com/r/LocalLLaMA/comments/1q094a3/qwenimage2512/)

**Author:** u/Nunki08 | **Upvotes:** 693 | **Comments:** 117 | **Date:** 2025-12-31

**Summary:** The post announces the release of Qwen-Image-2512, a new model available on multiple platforms with guides and GGUF files. It has received positive feedback from the community.

**Key Points:**
- Qwen-Image-2512 is available on platforms like Hugging Face, ModelScope, and GitHub.
- Guides and GGUF files are provided for easy access and use.
- The model has been well-received, with users testing it on low-end hardware.
- Demos and APIs are available for testing and integration.

**Discussion Highlights:** Users expressed gratitude for the new release and shared experiences of running the model on low-end hardware, highlighting its accessibility and performance.

---

## 22. [Update on the Llama 3.3 8B situation](https://reddit.com/r/LocalLLaMA/comments/1q06ddc/update_on_the_llama_33_8b_situation/)

**Author:** u/FizzarolliAI | **Upvotes:** 250 | **Comments:** 22 | **Date:** 2025-12-31

**Summary:** The post discusses updates on the Llama 3.3 8B model, including benchmark results for different configurations and the author's uncertainty about which version is more accurate. The author also expresses frustration with Meta's handling of the model's release.

**Key Points:**
- Benchmark results show the 128k context version outperforming the original 8k version.
- The author is unsure which version is more correct but recommends trying both.
- The author wishes Meta had officially released the weights.
- The post includes humor and self-deprecation, which some commenters appreciate.
- Some commenters discuss the implications of unofficial releases and the model's performance.

**Discussion Highlights:** The discussion includes appreciation for the author's work, humor, and debates about the model's performance and the implications of unofficial releases.

---

## 23. [[In the Wild] Reverse-engineered a Snapchat Sextortion Bot: It’s running a raw Llama-7B instance with a 2048 token window.](https://reddit.com/r/LocalLLaMA/comments/1pzwlie/in_the_wild_reverseengineered_a_snapchat/)

**Author:** u/simar-dmg | **Upvotes:** 717 | **Comments:** 106 | **Date:** 2025-12-30

**Summary:** A user reverse-engineered a Snapchat sextortion bot and discovered it was running a Llama-7B instance with a 2048 token window. The bot was vulnerable to persona-based attacks, revealing its configuration and malicious payload.

**Key Points:**
- The bot used a Llama-7B model with a 2048 token context window and high temperature setting.
- A persona-based attack (Grandma Protocol) successfully bypassed the bot's filters.
- The bot revealed environment variables and a malicious link when compromised.
- Scammers are using open-source models to avoid API costs and censorship filters.
- The community discussed the validity of the bot's responses and the likelihood of hallucinations.

**Discussion Highlights:** The discussion included skepticism about the bot's responses, with some users suggesting the information could be hallucinated. Others praised the user's methodology and findings.

---

## 24. [LLM server gear: a cautionary tale of a $1k EPYC motherboard sale gone wrong on eBay](https://reddit.com/r/LocalLLaMA/comments/1pzt1q8/llm_server_gear_a_cautionary_tale_of_a_1k_epyc/)

**Author:** u/__JockY__ | **Upvotes:** 195 | **Comments:** 81 | **Date:** 2025-12-30

**Summary:** The post discusses a seller's experience with eBay's dispute resolution process after selling a high-end EPYC motherboard. Despite providing detailed evidence and support, eBay initially sided with the buyer, highlighting the challenges sellers face on the platform.

**Key Points:**
- eBay's dispute resolution process heavily favors buyers, even with clear evidence.
- The seller provided high-quality photos and detailed support but still faced a dispute.
- The buyer claimed the motherboard was faulty, but the seller suspected improper installation.
- The process to resolve the dispute was intentionally cumbersome and frustrating.
- Other commenters shared similar experiences, reinforcing the consensus about eBay's seller-unfriendly policies.

**Discussion Highlights:** The discussion highlights a consensus among users about eBay's biased dispute resolution process, with many sharing similar experiences of unfair treatment as sellers. The post resonated with others who have faced similar challenges, emphasizing the platform's tendency to favor buyers.

---

## 25. [15M param model solving 24% of ARC-AGI-2 (Hard Eval). Runs on consumer hardware.](https://reddit.com/r/LocalLLaMA/comments/1pzsqii/15m_param_model_solving_24_of_arcagi2_hard_eval/)

**Author:** u/Doug_Bitterbot | **Upvotes:** 113 | **Comments:** 31 | **Date:** 2025-12-30

**Summary:** Bitterbot AI introduced TOPAS-DSPL, a 24M parameter model achieving 24% accuracy on ARC-AGI-2, using a dual-stream architecture to address compositional drift. The model is open-sourced and runs efficiently on consumer hardware like an RTX 4090.

**Key Points:**
- TOPAS-DSPL achieves 24% accuracy on ARC-AGI-2, significantly outperforming previous models of similar size.
- The model uses a dual-stream architecture (Logic and Canvas streams) to prevent compositional drift.
- It employs Test-Time Training (TTT) to fine-tune on specific puzzle examples before generating solutions.
- The community raised concerns about training on the test set and questioned comparisons with MuZero.
- Questions about scalability to larger parameter sizes were also discussed.

**Discussion Highlights:** The community showed mixed reactions, with some expressing excitement and others raising concerns about methodology and scalability. Key discussions included comparisons with MuZero, critiques about training on the test set, and inquiries about the model's potential at larger scales.

---

## 26. [Any guesses?](https://reddit.com/r/LocalLLaMA/comments/1pzhcqu/any_guesses/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 171 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** The Reddit post discusses speculation about upcoming Qwen model releases, with comments highlighting performance comparisons and new iterations like Qwen 6 and Qwen3vl-next-80b-a3b.

**Key Points:**
- Qwen 6 is speculated to outperform GPT 5.2 in key benchmarks
- Qwen3vl-next-80b-a3b is mentioned as a significant update without comparison issues
- Discussion includes references to Qwen image models and their iterations
- Community excitement about potential Qwen 3.5-235B-A10B release

**Discussion Highlights:** The discussion focuses on performance benchmarks and model iterations, with a consensus that Qwen models are making significant strides in AI capabilities.

---

## 27. [Running GLM-4.7 (355B MoE) in Q8 at ~5 Tokens/s on 2015 CPU-Only Hardware – Full Optimization Guide](https://reddit.com/r/LocalLLaMA/comments/1pzggbf/running_glm47_355b_moe_in_q8_at_5_tokenss_on_2015/)

**Author:** u/at0mi | **Upvotes:** 144 | **Comments:** 100 | **Date:** 2025-12-30

**Summary:** The post details how the author successfully ran the GLM-4.7 (355B MoE) model on a 2015 CPU-only system, achieving ~5 tokens/s using Q8 quantization. The setup involved extensive optimizations, including BIOS tweaks, NUMA node distribution, and Linux kernel adjustments, with a power draw of ~1300W. The author shared a detailed guide and invited discussion on similar CPU-only setups.

**Key Points:**
- GLM-4.7 (355B MoE) runs at ~5 tokens/s on a 2015 Lenovo System x3950 X6 with 8 Xeon E7-8880 v3 CPUs.
- Optimizations included BIOS settings, NUMA node distribution, and Linux kernel tweaks.
- Power consumption is ~1300W under full load.
- Cost estimate for a similar system is around £2,500.
- Discussion highlights energy efficiency and performance trade-offs.

**Discussion Highlights:** The discussion focused on energy efficiency (e.g., 60 kWh per 1M tokens) and cost considerations, with some users noting concerns about power draw and performance limitations without a GPU. Others shared cost estimates for building similar systems.

---

## 28. [Tencent HY-Motion 1.0 - a billion-parameter text-to-motion model](https://reddit.com/r/LocalLLaMA/comments/1pzcrtb/tencent_hymotion_10_a_billionparameter/)

**Author:** u/ResearchCrafty1804 | **Upvotes:** 318 | **Comments:** 36 | **Date:** 2025-12-30

**Summary:** Tencent has open-sourced HY-Motion 1.0, a billion-parameter text-to-motion model that generates high-fidelity 3D animations from natural language. It features a comprehensive training strategy and covers 200+ motion categories, aiming to streamline 3D animation workflows.

**Key Points:**
- HY-Motion 1.0 is a billion-parameter text-to-motion model based on Diffusion Transformer (DiT) architecture.
- It uses a full-stage training strategy (Pre-training → SFT → RL) to optimize motion quality and semantic accuracy.
- The model covers 200+ motion categories across 6 major classes, making it highly versatile.
- Users report it works well for game development with minimal cleanup required.
- Questions remain about its compatibility with non-humanoid models like animals.

**Discussion Highlights:** The community is excited about the model's potential, especially for game development. Some users have successfully tested it and confirmed its effectiveness, while others are curious about its applicability to non-humanoid models. There is also humor about potential uses in adult content creation.

---

## 29. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7mxr/llama338binstruct/)

**Author:** u/ttkciar | **Upvotes:** 149 | **Comments:** 25 | **Date:** 2025-12-29

**Summary:** The post discusses the release of Llama-3.3-8B-Instruct, a potentially new model, with links to its Hugging Face repositories and GGUF files. The community expresses excitement and skepticism about its authenticity.

**Key Points:**
- Llama-3.3-8B-Instruct model release with Hugging Face links provided
- Community excitement and skepticism about the model's authenticity
- Ongoing sanity check benchmarks to verify if it's a newer version
- Mentions of updated rope config for full context length
- Desire for updated 70B or new 30B models

**Discussion Highlights:** The discussion highlights a mix of excitement and skepticism about the Llama-3.3-8B-Instruct model. Key points include ongoing verification efforts, technical details about the model's configuration, and community interest in larger model variants.

---

## 30. [Llama-3.3-8B-Instruct](https://reddit.com/r/LocalLLaMA/comments/1pz7bmv/llama338binstruct/)

**Author:** u/jacek2023 | **Upvotes:** 461 | **Comments:** 78 | **Date:** 2025-12-29

**Summary:** The post discusses the discovery and release of the Llama-3.3-8B-Instruct model, which was obtained through Meta's finetuning API. The author details their experience navigating the API's bugs and limitations to download the model.

**Key Points:**
- Llama-3.3-8B-Instruct model is now available via GGUF format.
- The model was obtained through Meta's finetuning API, which had hidden and buggy features.
- The author extracted the original model by removing the finetuned adapter.
- Community members are verifying the model's authenticity and performance.
- Discussion includes technical details like position embeddings and ongoing evaluations.

**Discussion Highlights:** The community is enthusiastic about the release, with efforts focused on verifying the model's authenticity and comparing it to other Llama versions. Some users are running benchmarks and evaluations to assess its performance.

---

## 31. [Z AI is going for an IPO on Jan 8 and set to raise $560 million. Z.ai is set to be the first AI-native LLM company to list on the global market.](https://reddit.com/r/LocalLLaMA/comments/1pz68fz/z_ai_is_going_for_an_ipo_on_jan_8_and_set_to/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 343 | **Comments:** 120 | **Date:** 2025-12-29

**Summary:** Z AI is set to go public on January 8, aiming to raise $560 million, marking it as the first AI-native LLM company to list globally. The announcement has sparked discussions about the future of open-source AI models.

**Key Points:**
- Z AI's IPO is scheduled for January 8, 2026, with a target of raising $560 million.
- Concerns about the future of open-source AI models post-IPO.
- Debate on whether Z AI will continue releasing open weight models.
- Mixed reactions from the community, with some expressing concerns about commercialization.

**Discussion Highlights:** The community discussion highlights a divide between those who fear the end of open-source contributions and those who believe commercial success is necessary for sustainability. Some users argue that paid subscriptions could be more accessible than investing in GPUs for individual projects.

---

## 32. [Naver (South Korean internet giant), has just launched HyperCLOVA X SEED Think, a 32B open weights reasoning model and HyperCLOVA X SEED 8B Omni, a unified multimodal model that brings text, vision, and speech together](https://reddit.com/r/LocalLLaMA/comments/1pyjjbw/naver_south_korean_internet_giant_has_just/)

**Author:** u/Nunki08 | **Upvotes:** 162 | **Comments:** 31 | **Date:** 2025-12-29

**Summary:** Naver has launched two new AI models: HyperCLOVA X SEED Think 32B, a 32B open weights reasoning model, and HyperCLOVA X SEED 8B Omni, a unified multimodal model integrating text, vision, and speech. The announcement has generated significant interest in the AI community.

**Key Points:**
- HyperCLOVA X SEED Think 32B is a 32B open weights reasoning model.
- HyperCLOVA X SEED 8B Omni is a multimodal model combining text, vision, and speech.
- The community is interested in the models' capabilities and compatibility with existing tools like llama.cpp and vLLM.
- There is excitement about the potential for audio-to-audio functionality.
- The models are part of a series of new AI releases from Korea.

**Discussion Highlights:** The community discussion highlights enthusiasm for the multimodal capabilities of the HyperCLOVA X SEED 8B Omni model, with questions about its compatibility with existing AI tools and frameworks. There is also interest in the potential for audio-to-audio functionality and the broader context of new AI models emerging from Korea.

---

## 33. [Tencent just released WeDLM 8B Instruct on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyg4yt/tencent_just_released_wedlm_8b_instruct_on/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 422 | **Comments:** 62 | **Date:** 2025-12-29

**Summary:** Tencent released WeDLM 8B Instruct on Hugging Face, a diffusion language model that runs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks. The release has generated significant interest and discussion in the community.

**Key Points:**
- WeDLM 8B Instruct is a diffusion language model released by Tencent on Hugging Face.
- It performs 3-6× faster than vLLM-optimized Qwen3-8B on math reasoning tasks.
- The model is released under the Apache 2.0 license.
- There is also a 7B version available.
- The community shows strong interest and positive feedback on the release.

**Discussion Highlights:** The community is excited about the performance and potential of the WeDLM models, with many users expressing interest in the Apache 2.0 license and the availability of both 7B and 8B versions. Some users are surprised by the effectiveness of diffusion models for language tasks.

---

## 34. [Meta released RPG, a research plan generation dataset on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pyao6g/meta_released_rpg_a_research_plan_generation/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 258 | **Comments:** 21 | **Date:** 2025-12-28

**Summary:** Meta released the RPG dataset on Hugging Face, featuring 22k tasks across ML, Arxiv, and PubMed, with evaluation rubrics and Llama-4 reference solutions for training AI co-scientists.

**Key Points:**
- RPG dataset includes 22k tasks spanning ML, Arxiv, and PubMed
- Dataset comes with evaluation rubrics and Llama-4 reference solutions
- Aimed at training AI co-scientists
- Meta's open-source contributions are seen as competitive with OpenAI
- Research plan generation is crucial for agentic and tool-using systems

**Discussion Highlights:** The discussion highlights Meta's strong open-source contributions, with comparisons to OpenAI. Users appreciate the dataset's potential for improving AI planning capabilities, though some note the importance of releasing models trained on such datasets.

---

