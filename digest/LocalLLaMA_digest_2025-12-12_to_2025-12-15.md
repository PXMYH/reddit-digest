# r/LocalLLaMA Reading Digest

**Period:** 2025-12-12 to 2025-12-15
**Posts Summarized:** 15
**Total Posts Analyzed:** 15

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1302 | **Comments:** 151 | **Date:** 2025-12-12

**Summary:** An NVIDIA employee accidentally uploaded the parent folder of their upcoming model on Hugging Face, sparking interest and concern among users.

**Key Points:**
- Accidental upload of NVIDIA's upcoming model files on Hugging Face
- Users expressed interest in saving the files before potential takedown
- Mentions of specific models like Nano and 30B-A3B
- Positive sentiment towards the Nemotron lineup
- Concerns about potential censorship of the uploaded content

**Discussion Highlights:** The discussion highlights a mix of excitement about the accidental leak and concerns about the files being taken down. Users are interested in the potential of the models mentioned, such as Nano and 30B-A3B, and appreciate the Nemotron lineup. There is a consensus to save the files before any censorship is implemented.

---

## 2. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 868 | **Comments:** 176 | **Date:** 2025-12-14

**Summary:** The Reddit post discusses the end of a product or service, with users expressing mixed reactions ranging from humor to indifference. The discussion highlights varying perspectives on the significance of the event.

**Key Points:**
- The post is a link with no text content, indicating a significant event or announcement.
- Users react with humor, such as buying more storage or referencing memes.
- Some users downplay the significance, noting it's not a major issue.
- The discussion includes a mix of sarcasm and practical observations.

**Discussion Highlights:** The discussion is marked by a mix of humor and indifference. Some users see it as a non-issue, while others joke about stocking up on resources. There is no clear consensus, but the overall tone is lighthearted.

---

## 3. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 698 | **Comments:** 77 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800s London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- The dataset consists of 90GB with 135,000 documents from 1800-1875 London texts.
- A bias report covering temporal, gender/pronoun, and geographic bias has been generated.
- A small evaluation model (300M parameters) was trained on a 15GB subset to evaluate the dataset.
- The community appreciates the detailed work and suggests considering MoE for better compute efficiency.
- The project aims to study historical biases and train an LLM specific to 1800s London texts.

**Discussion Highlights:** The community shows strong support for the project, with suggestions to consider Mixture of Experts (MoE) for better compute efficiency. There is also interest in whether older texts reprinted in the 1800s were included in the dataset.

---

## 4. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 619 | **Comments:** 269 | **Date:** 2025-12-13

**Summary:** The author details their journey upgrading a GPU server from a single 3080 to an 8x RTX Pro 6000 setup with a Threadripper PRO 9955WX and 384 GB RAM, facing challenges like overheating and power management. The post highlights the iterative process of hardware upgrades and the complexities of scaling GPU setups.

**Key Points:**
- Upgraded from a single 3080 to 8x RTX Pro 6000 GPUs with a Threadripper PRO 9955WX and 384 GB RAM
- Faced overheating issues with dual 4090s, leading to a larger case and new host
- Encountered IOMMU addressing issues with 4x RTX Pro 6000, requiring a workaround with two systems
- Community reactions include admiration, criticism of the setup's cooling and power management, and suggestions for server-grade hardware
- Discussion highlights the trade-offs between consumer and server-grade hardware for high-performance computing

**Discussion Highlights:** The community expressed a mix of admiration for the setup's power and criticism of its cooling and power management. Some suggested using server-grade hardware and rack-mounted solutions for better efficiency and reliability. The discussion also touched on the challenges of scaling consumer hardware for high-performance computing tasks.

---

## 5. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 608 | **Comments:** 111 | **Date:** 2025-12-13

**Summary:** OpenAI's ChatGPT-5.2 model is ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and processing clinical notes for QA evaluation.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report issues with follow-up questions and research capabilities compared to previous versions.
- Difficulties in processing made-up clinical notes for QA model evaluation.
- Questions about the testing criteria for the Sansa benchmark.
- Observations about Gemini being less censored than other models, including Mistral.

**Discussion Highlights:** Users express concerns about the performance and censorship of ChatGPT-5.2, comparing it unfavorably to previous versions and other models like Gemini and Mistral. There is curiosity about the benchmark testing criteria and the reasons behind the censorship rankings.

---

## 6. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 575 | **Comments:** 118 | **Date:** 2025-12-12

**Summary:** The user shares their upgraded 'Monster server' setup, featuring a Ryzen 3950x CPU, 128GB RAM, and three GPUs (2x RTX 3090 and 1x RTX 4090). The server is used for running local LLMs like GPT-OSS-120B and other tasks, with a focus on performance and cost-effectiveness. Key points include the hardware specifications, the use of an M.2 to PCIe adapter for the RTX 4090, and the user's 10GB fiber internet. Discussion highlights include nostalgia for early 2000s overclocking forums, questions about the user's location for affordable internet, technical feedback on GPU setup efficiency, and curiosity about heat management and the second PSU setup.

---

## 7. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 356 | **Comments:** 40 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations for Qwen3, specifically an autoregressive delta net computation that improves generation speed by 40%. The author invites others to test the optimization.

**Key Points:**
- Optimized autoregressive delta net computation for Qwen3
- 40% generation speed improvement reported
- Optimizations include removing unnecessary reshapes and computations
- Community appreciation and interest in further optimizations
- Questions about compatibility with ROCm/Vulkan

**Discussion Highlights:** The community shows strong appreciation for the optimization work, with comments highlighting the author's frequent contributions and interest in further improvements. There is a question about whether the speedup applies to ROCm/Vulkan in addition to CUDA.

---

## 8. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 288 | **Comments:** 35 | **Date:** 2025-12-12

**Summary:** The Reddit post discusses the feasibility and performance of running an LLM on a 3DS, drawing comparisons to similar projects on platforms like the PS Vita and Wii. The community expresses enthusiasm and curiosity about the technical possibilities.

**Key Points:**
- Running an LLM on a 3DS is technically feasible, as demonstrated by similar projects on other platforms.
- The community is impressed by the project, with comparisons to running LLMs on the PS Vita and Wii.
- Performance considerations are discussed, including potential improvements on a 'new' 3DS.
- There is curiosity about the potential for AI-driven games on older hardware.

**Discussion Highlights:** The discussion highlights the technical achievements of running LLMs on older hardware, with community members expressing admiration and curiosity about performance optimizations and potential applications.

---

## 9. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 238 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve throughput during text generation using Eagle3 speculative decoding. It is licensed for both commercial and non-commercial use.

**Key Points:**
- GPT-OSS-120B-Eagle3-throughput is an optimized speculative decoding module built on OpenAI's gpt-oss-120b base model.
- It uses NVIDIA’s Eagle3 speculative decoding approach to predict a single draft token efficiently.
- The model is licensed under the nvidia-open-model-license for commercial and non-commercial use.
- It is intended for applications like AI agents, chatbots, and retrieval-augmented generation (RAG) systems.
- The model is not supported in llama.cpp, as indicated by a stale feature request.

**Discussion Highlights:** The discussion includes interest in making the model derestricted, questions about its compatibility with CPU inference, and mentions of its lack of support in llama.cpp. There is also a humorous comment about waiting for a REAP EAGLE3 HERETIC MOE GGUF version.

---

## 10. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 236 | **Comments:** 77 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which users find inconsistent and unappealing.

**Key Points:**
- OpenAI's advertising shift from AI advancements to astrology ads
- Criticism of the inconsistency in OpenAI's messaging
- Discussion on the profitability of targeting non-technical audiences
- Suggestions for alternative advertising strategies
- Observations on the perceived decline in OpenAI's reputation

**Discussion Highlights:** The discussion highlights a consensus that OpenAI's new advertising approach is seen as a misstep, with users expressing disappointment and suggesting more effective strategies.

---

## 11. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 178 | **Comments:** 28 | **Date:** 2025-12-12

**Summary:** The post introduces Olmo 3.1 32B Think and Instruct models, highlighting their specialized capabilities in deep reasoning and instruction following, respectively. The community responds positively, praising the models' open-source nature and anticipating future developments.

**Key Points:**
- Olmo 3.1 32B Think model excels in multi-step reasoning, math, logic, and code generation.
- Olmo 3.1 32B Instruct model is optimized for instruction following, conversational fluency, and tool-use capabilities.
- Community appreciates the open-source nature and continuous improvement of Olmo models.
- Expectations for future developments, such as Mixture of Experts (MOE) models.
- Positive feedback on the educational value of the accompanying paper.

**Discussion Highlights:** The community discussion is largely positive, with users expressing excitement about the new models and their capabilities. There is a strong appreciation for the open-source nature of the Olmo models and the educational value of the accompanying paper. Some users are anticipating future developments, such as the introduction of Mixture of Experts (MOE) models.

---

## 12. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 169 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that they share nearly identical sizes and architectures, with minor differences in expert configurations. The community highlights the open-source nature of these models and their adoption by various teams.

**Key Points:**
- Mistral 3 Large and DeepSeek V3 have almost identical sizes (671B vs 673B).
- Mistral 3 Large uses the same architecture as DeepSeek V3 but with adjusted expert configurations.
- Mistral likely trained their model from scratch due to using a different tokenizer.
- The DeepSeek V3 architecture is being widely adopted by other models like Kimi K2 and Gigachat.
- The community views this as a positive aspect of open-source collaboration.

**Discussion Highlights:** The discussion highlights the open-source spirit, with multiple models adopting the DeepSeek V3 architecture. Users appreciate the innovation and resource efficiency of the architecture, while also noting Mistral's additional work on multimodal capabilities.

---

## 13. [Understanding the new router mode in llama cpp server](https://reddit.com/r/LocalLLaMA/comments/1pmc7lk/understanding_the_new_router_mode_in_llama_cpp/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 161 | **Comments:** 44 | **Date:** 2025-12-14

**Summary:** Router mode in llama cpp server allows managing multiple AI models simultaneously without restarting the server, similar to Ollama's functionality. It enables dynamic loading/unloading of models and routing requests to the appropriate model, saving memory and simplifying model switching.

**Key Points:**
- Router mode enables managing multiple AI models in a single server process
- Models can be loaded/unloaded on demand without restarting the server
- Requests are routed to the appropriate model internally
- Saves memory and simplifies switching between models
- Useful for testing multiple GGUF models and building local OpenAI-compatible APIs

**Discussion Highlights:** Users are generally positive about the new router mode, comparing it to existing solutions like llama-swap. Some users expressed interest in advanced features like VRAM management for multiple GPUs and the ability to specify which models stay in memory concurrently.

---

## 14. [To Mistral and other lab employees: please test with community tools BEFORE releasing models](https://reddit.com/r/LocalLLaMA/comments/1pmgm2x/to_mistral_and_other_lab_employees_please_test/)

**Author:** u/dtdisapointingresult | **Upvotes:** 137 | **Comments:** 71 | **Date:** 2025-12-14

**Summary:** The Reddit post criticizes Mistral for releasing Devstral 2 without thorough testing with community tools, which led to issues like benchmark discrepancies and repetition loops. The author emphasizes the importance of testing with local tools to maintain reputation and user trust. Key points include the lack of testing with community tools, issues with benchmark discrepancies and repetition loops, and the importance of testing with local tools. The discussion highlights mixed feedback, with some users reporting positive experiences with Devstral 2 in various applications, while others acknowledge the need for adjustments and testing with local tools. There is a consensus on the importance of thorough testing before release to avoid reputational damage.

---

## 15. [Qwen3-Next-80B-A3B-Thinking-GGUF has just been released on HuggingFace](https://reddit.com/r/LocalLLaMA/comments/1pmo0dn/qwen3next80ba3bthinkinggguf_has_just_been/)

**Author:** u/LegacyRemaster | **Upvotes:** 123 | **Comments:** 52 | **Date:** 2025-12-14

**Summary:** The Reddit post announces the release of Qwen3-Next-80B-A3B-Thinking-GGUF on HuggingFace, highlighting its impressive performance in a Tetris game implemented in a single HTML file. Users compare it favorably to other models like Devstral and discuss its capabilities and release timing.

**Key Points:**
- Qwen3-Next-80B-A3B-Thinking-GGUF model released on HuggingFace
- Model excels in generating a Tetris game in a single HTML file
- Performance compared favorably to Devstral
- Users discuss the model's release timing and capabilities
- Technical queries about tool support (e.g., llamacpp)

**Discussion Highlights:** Users express amazement at the model's capabilities, with some noting its potential for agentic coding tasks. There is debate about the release timing, and technical questions about tool compatibility are raised.

---

