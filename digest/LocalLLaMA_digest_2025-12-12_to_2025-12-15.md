# r/LocalLLaMA Reading Digest

**Period:** 2025-12-12 to 2025-12-15
**Posts Summarized:** 15
**Total Posts Analyzed:** 15

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1283 | **Comments:** 149 | **Date:** 2025-12-12

**Summary:** An NVIDIA employee accidentally uploaded the parent folder of an upcoming model on Hugging Face, sparking significant interest and urgency within the community to preserve the leaked content.

**Key Points:**
- Accidental upload of NVIDIA's upcoming model parent folder on Hugging Face
- Community urgency to save the content before potential takedown
- Mentions of specific models like Nano and 30B-A3B
- Positive sentiment towards the Nemotron lineup and related projects
- Concerns about censorship and the need to act quickly

**Discussion Highlights:** The community showed strong interest in preserving the leaked content, with discussions highlighting the potential value of the models and the urgency to act before any censorship or takedown.

---

## 2. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 660 | **Comments:** 71 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800s London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- 90GB dataset with 135,000 documents from 1800-1875 London texts
- Bias report covering temporal, gender/pronoun, and geographic bias
- Evaluation model trained on a 15GB subset (300M parameters, 10K steps)
- Community appreciation and suggestions for improvement
- Discussion on dataset inclusion criteria and model architecture

**Discussion Highlights:** The community shows strong support for the project, with suggestions for dataset refinement and model architecture improvements. There is interest in the project's progress and potential applications.

---

## 3. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 602 | **Comments:** 264 | **Date:** 2025-12-13

**Summary:** The Reddit post details a user's journey upgrading their GPU server, culminating in a system with 8x RTX Pro 6000 GPUs, a Threadripper PRO 9955WX CPU, and 384 GB RAM, totaling 768 GB VRAM. The user faced challenges with heat management, power consumption, and hardware compatibility during the upgrades.

**Key Points:**
- User upgraded from a single 3080 to 8x RTX Pro 6000 GPUs over time.
- Final setup includes Threadripper PRO 9955WX CPU and 384 GB RAM.
- Faced issues with overheating, power consumption, and motherboard compatibility.
- Community reactions include admiration, criticism of the setup's physical implementation, and suggestions for server-grade hardware.
- Discussion highlights include concerns about power supply reliability and the practicality of the setup.

**Discussion Highlights:** The community expressed a mix of admiration for the powerful setup and criticism regarding its physical implementation, such as the use of a consumer-grade case and makeshift cooling solutions. Some users suggested using server-grade hardware and proper rack mounting for better reliability and safety. There was also discussion about power supply challenges and the practicality of such a high-power setup in a non-server environment.

---

## 4. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 598 | **Comments:** 106 | **Date:** 2025-12-13

**Summary:** OpenAI's ChatGPT-5.2 model is ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and clinical note generation compared to previous versions.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report issues with follow-up questions and research capabilities.
- Problems with generating clinical notes for QA model evaluation.
- Curiosity about the testing criteria given Grok's low ranking.
- Observations about Gemini being less censored than other models.

**Discussion Highlights:** Users express dissatisfaction with ChatGPT-5.2's performance in follow-up questions and research, as well as its increased censorship compared to previous models. There is curiosity about the benchmark testing criteria and observations about other models' censorship levels.

---

## 5. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 573 | **Comments:** 116 | **Date:** 2025-12-12

**Summary:** The user shares their upgraded 'Monster-server,' a powerful homelab setup with multiple GPUs for running local LLMs. The server features a Ryzen 3950x CPU, 128GB RAM, and three GPUs (2x RTX 3090 and 1x RTX 4090), along with high-speed storage and a 10GBe NIC. The setup is praised for its performance and nostalgia factor.

**Key Points:**
- The server uses a Ryzen 3950x CPU and 128GB RAM, with three GPUs (2x RTX 3090 and 1x RTX 4090).
- The user runs GPT-OSS-120B fully in VRAM, achieving over 100 tokens per second.
- The setup includes a 10GBe NIC and high-capacity storage (8TB NVMe and 4x 18TB HDDs).
- Comments highlight nostalgia for early 2000s overclocking forums and curiosity about the user's location for affordable 10GBe internet.
- Some discussion points out potential inefficiencies in a 3-GPU setup compared to 2 or 4 GPUs.

**Discussion Highlights:** The discussion includes nostalgia for early 2000s tech forums, curiosity about the user's location for affordable high-speed internet, and technical observations about GPU setup efficiency.

---

## 6. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 536 | **Comments:** 108 | **Date:** 2025-12-14

**Summary:** The Reddit post discusses the discontinuation or decline of SATA SSDs, with comments highlighting their niche status and the preference for M.2 interfaces.

**Key Points:**
- Post title suggests the end of something
- Comments mention Discord features and SSD purchases
- Discussion focuses on SATA SSDs becoming niche
- M.2 is preferred for flash storage

**Discussion Highlights:** The discussion consensus is that SATA SSDs are becoming less relevant, with M.2 being the better interface for flash storage.

---

## 7. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 353 | **Comments:** 39 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations made to Qwen3, specifically an autoregressive delta net computation that improves generation speed by 40%. The author invites others to test the optimizations and share their results.

**Key Points:**
- Optimized autoregressive delta net computation for Qwen3
- 40% generation speed improvement reported
- Optimizations include removing unnecessary reshapes and computations
- Author invites community testing and feedback
- Positive community response with appreciation for the contribution

**Discussion Highlights:** The community responded positively, with comments appreciating the contribution and asking about compatibility with different platforms like ROCm/Vulkan. There was also humor about the author's frequent contributions and excitement for future optimizations.

---

## 8. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 287 | **Comments:** 32 | **Date:** 2025-12-12

**Summary:** The Reddit post discusses the feasibility and novelty of running an LLM on a 3DS, drawing comparisons to similar projects on other platforms like the PS Vita and Wii. The community expresses admiration for the technical achievement and curiosity about performance improvements on newer hardware.

**Key Points:**
- Running an LLM on a 3DS is a notable technical achievement.
- Comparisons are made to similar projects on PS Vita and Wii.
- Community members are impressed and curious about performance on newer hardware.
- The project sparks discussions about the potential of AI in gaming devices.

**Discussion Highlights:** The discussion highlights the novelty of running an LLM on a 3DS, with community members expressing admiration for the technical feat. There is curiosity about performance improvements on newer hardware and the potential for AI integration in gaming devices.

---

## 9. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 238 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve throughput during text generation using Eagle3 speculative decoding. It is intended for both commercial and non-commercial use in various AI applications.

**Key Points:**
- GPT-OSS-120B-Eagle3-throughput is an optimized speculative decoding module built on OpenAI's gpt-oss-120b base model.
- It uses NVIDIA’s Eagle3 speculative decoding approach to predict a single draft token efficiently.
- The model is licensed under the nvidia-open-model-license for commercial and non-commercial use.
- It is useful for high-concurrency inference scenarios where fast token generation is a priority.
- The model is not supported in llama.cpp, as indicated by a stale feature request.

**Discussion Highlights:** The discussion highlights include appreciation for the post's popularity, inquiries about making the model derestricted, and mentions of its lack of support in llama.cpp. There is also a humorous comment about waiting for a REAP EAGLE3 HERETIC MOE GGUF version.

---

## 10. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 233 | **Comments:** 76 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which users find inconsistent and unappealing. Key points include the criticism of OpenAI's shift to astrology ads, the inconsistency with previous messaging, the potential profitability of targeting astrology believers over programmers, the consensus on the significant fall from grace, and questions about the effectiveness of the ads. The discussion highlights a consensus that OpenAI's shift to astrology ads is seen as a significant fall from grace and inconsistent with their previous messaging about advanced AI. Users also question the effectiveness of these ads in attracting genuine horoscope believers.

---

## 11. [First AI implosion: Oracle](https://reddit.com/r/LocalLLaMA/comments/1pmfglp/first_ai_implosion_oracle/)

**Author:** u/Terminator857 | **Upvotes:** 231 | **Comments:** 186 | **Date:** 2025-12-14

**Summary:** The post discusses Oracle's potential financial instability due to its debt-driven AI expansion, suggesting it might be the first major tech company to face difficulties. The author also speculates about the end of a RAM shortage and invites discussion on the topic.

**Key Points:**
- Oracle's financial risk due to its debt-reliant expansion in AI
- Potential end of the RAM shortage sooner than expected
- Community frustration with AI-generated social media content
- Oracle's historical dominance in enterprise software and its financial resilience
- Comparison of Oracle's financial situation with other tech giants like Google and Microsoft

**Discussion Highlights:** The discussion highlights skepticism about Oracle's stability despite its historical strength, with some users expressing frustration over AI-generated content. There is also a consensus that Oracle's debt-reliant expansion makes it more vulnerable compared to companies with stronger cash flows like Google and Microsoft.

---

## 12. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 173 | **Comments:** 24 | **Date:** 2025-12-12

**Summary:** Olmo 3.1 32B Think and Instruct are new 32-billion-parameter models in the Olmo family, optimized for deep reasoning and instruction following, respectively. The Think model excels in multi-step reasoning and code generation, while the Instruct model focuses on conversational fluency and tool-use capabilities.

**Key Points:**
- Olmo 3.1 32B Think is optimized for deep reasoning, math, logic, and code generation.
- Olmo 3.1 32B Instruct is optimized for instruction following, conversational fluency, and tool-use capabilities.
- Both models are fully open source and part of the Olmo family.
- The community appreciates the models' openness and continuous improvement.
- There is anticipation for future developments, such as MOE (Mixture of Experts).

**Discussion Highlights:** The community is positive about the new models, appreciating their open-source nature and the educational value of the accompanying paper. There is also anticipation for future advancements like MOE.

---

## 13. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 166 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that they share nearly identical sizes and architectures. The author highlights that Mistral 3 Large reuses the DeepSeek V3 architecture but likely trained it from scratch using their own tokenizer. The discussion includes comments about other models using the same architecture and the spirit of open source. Key points include: Mistral 3 Large and DeepSeek V3 have almost identical sizes (671B vs 673B); Mistral 3 Large uses the same architecture as DeepSeek V3/V3.1 but with adjusted expert sizes and numbers; Mistral likely trained their model from scratch rather than fine-tuning DeepSeek V3; Other models like Kimi K2 and Gigachat also use the DeepSeek V3 architecture; The discussion highlights the benefits and spirit of open-source collaboration. The discussion emphasizes the open-source nature of the DeepSeek V3 architecture, with multiple models adopting it due to its proven effectiveness. Comments highlight the innovation within the open-source community and the practical benefits of reusing well-researched architectures.

---

## 14. [Understanding the new router mode in llama cpp server](https://reddit.com/r/LocalLLaMA/comments/1pmc7lk/understanding_the_new_router_mode_in_llama_cpp/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 145 | **Comments:** 34 | **Date:** 2025-12-14

**Summary:** Router mode in llama cpp server allows managing multiple AI models simultaneously without restarting the server, similar to Ollama's functionality. It enables loading/unloading models on demand and routing requests to the appropriate model, saving memory and simplifying model switching.

**Key Points:**
- Router mode enables managing multiple AI models with a single server process
- Models can be loaded/unloaded on demand, reducing memory usage
- Requests are routed to the appropriate model automatically
- Useful for testing multiple GGUF models and building local OpenAI-compatible APIs
- Simplifies switching between small and large models dynamically

**Discussion Highlights:** Users compared router mode to existing tools like llama-swap, discussed VRAM management for multiple GPUs, and expressed interest in specifying which models stay in memory concurrently. Some users found the explanatory image unhelpful.

---

## 15. [To Mistral and other lab employees: please test with community tools BEFORE releasing models](https://reddit.com/r/LocalLLaMA/comments/1pmgm2x/to_mistral_and_other_lab_employees_please_test/)

**Author:** u/dtdisapointingresult | **Upvotes:** 125 | **Comments:** 69 | **Date:** 2025-12-14

**Summary:** The Reddit post criticizes Mistral for releasing Devstral 2 without thorough testing with community tools, leading to issues like benchmark discrepancies and repetition loops. The author emphasizes the importance of testing with local tools to maintain reputation and user trust.

**Key Points:**
- Devstral 2 release faced issues due to lack of testing with community tools.
- Mistral's reputation was affected by problems like benchmark discrepancies and repetition loops.
- The author stresses the importance of testing with local tools before release.
- Community tools like Llama.cpp and MLX-Engine often require adjustments for new models.
- Positive feedback exists for Devstral 2 123b, indicating successful use with local tools.

**Discussion Highlights:** The discussion highlights mixed experiences with Devstral 2, with some users reporting successful use with local tools while others faced issues. There is a consensus on the need for better testing and documentation to ensure smooth integration with community tools.

---

