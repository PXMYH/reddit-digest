# r/LocalLLaMA Reading Digest

**Period:** 2025-12-12 to 2025-12-15
**Posts Summarized:** 15
**Total Posts Analyzed:** 15

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1297 | **Comments:** 150 | **Date:** 2025-12-12

**Summary:** A user from NVIDIA accidentally uploaded the parent folder of an upcoming model on Hugging Face, sparking a discussion about the potential leak and the importance of saving the content before it gets taken down.

**Key Points:**
- NVIDIA employee mistakenly uploaded a parent folder of an upcoming model on Hugging Face.
- The post gained significant attention with 1297 upvotes and 150 comments.
- Users expressed concern about the content being taken down and encouraged others to save it.
- The Nemotron lineup was mentioned as promising.
- There was a sense of urgency to grab the content before full censoring.

**Discussion Highlights:** The discussion highlighted the community's interest in the leaked content, with many users emphasizing the need to save the material before it gets removed. There was also appreciation for the Nemotron lineup and the potential of the projects mentioned.

---

## 2. [Aaaand... is gone...](https://reddit.com/r/LocalLLaMA/comments/1pmungj/aaaand_is_gone/)

**Author:** u/HumanDrone8721 | **Upvotes:** 833 | **Comments:** 169 | **Date:** 2025-12-14

**Summary:** The Reddit post discusses the apparent discontinuation or shortage of certain storage drives, sparking a mix of concern and humor among users. The discussion highlights varying perspectives on the impact of this development.

**Key Points:**
- The post title suggests something is no longer available
- Users joke about buying more storage in response
- Discussion includes references to SATA drives and their relevance
- Some users downplay the significance of the news

**Discussion Highlights:** The discussion features a range of reactions, from humorous remarks about purchasing additional storage to debates about the actual impact of the news on SATA drives. The overall tone is mixed, with some users seeing it as a minor issue and others as an opportunity.

---

## 3. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 676 | **Comments:** 72 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800-1875 London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- The dataset consists of 90GB with 135,000 documents from 1800-1875 London texts.
- A bias report covering temporal, gender/pronoun, and geographic bias has been generated.
- A small evaluation model (300M parameters) was trained on a 15GB subset to evaluate the dataset.
- The community appreciates the work and suggests considering Mixture of Experts (MoE) for better compute efficiency.
- The project aims to study historical texts despite inherent biases.

**Discussion Highlights:** The community shows strong support for the project, with suggestions for improving efficiency and interest in the progress of the 1800s LLM initiative.

---

## 4. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 612 | **Comments:** 268 | **Date:** 2025-12-13

**Summary:** The user detailed their journey upgrading a GPU server from a single 3080 to an 8x RTX Pro 6000 setup with a Threadripper PRO 9955WX and 384 GB RAM, facing challenges like overheating and power management. The post highlights the iterative process of hardware upgrades and the eventual solution involving multiple systems and network configurations.

**Key Points:**
- Upgraded from a single 3080 to 8x RTX Pro 6000 GPUs with a Threadripper PRO 9955WX and 384 GB RAM
- Faced overheating issues with dual 4090s, leading to a larger case and new host
- Encountered IOMMU addressing issues with 4x RTX Pro 6000, requiring a workaround with two systems
- Community reactions included admiration, criticism of the setup's physical configuration, and suggestions for server-grade hardware
- Discussion highlighted concerns about power management and hardware reliability

**Discussion Highlights:** The community expressed a mix of admiration for the setup's power and criticism of its physical configuration, with suggestions to use server-grade hardware and proper rack mounting. There were also discussions about power management and hardware reliability, with some users sharing their experiences with similar high-power setups.

---

## 5. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 607 | **Comments:** 111 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses OpenAI's ChatGPT-5.2 model being ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and clinical note generation.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report the model performs poorly on follow-up questions and research tasks compared to previous versions.
- Difficulties in generating clinical notes for QA model evaluation.
- Questions about the testing criteria for the Sansa benchmark.
- Observations that Gemini is less censored than other models.

**Discussion Highlights:** Users express dissatisfaction with ChatGPT-5.2's performance in follow-up questions and research tasks, noting a decline from previous versions. There are also concerns about the model's ability to handle clinical note generation and questions about the benchmark's testing criteria. Some users find it surprising that Gemini is ranked as less censored than other models.

---

## 6. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 575 | **Comments:** 118 | **Date:** 2025-12-12

**Summary:** The author shares their upgraded 'Monster-server,' a powerful homelab setup featuring a Ryzen 3950x CPU, 128GB RAM, and three GPUs (2x RTX 3090 and 1x RTX 4090). The server runs local LLMs like GPT-OSS-120B and is used for research and coding. The post highlights the hardware configuration, storage, and networking capabilities. Key points include the server's hardware specifications, storage setup, performance metrics, and networking capabilities. The discussion highlights nostalgia for early 2000s overclocking forums, curiosity about the author's location due to affordable 10GB internet, and technical feedback on GPU setup efficiency.

---

## 7. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 358 | **Comments:** 40 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations made to Qwen3, resulting in a 40% generation speed upgrade. The author implemented an optimized autoregressive delta net computation and removed unnecessary operations.

**Key Points:**
- Optimized autoregressive delta net computation for faster performance
- Removed unnecessary reshapes and operations
- Reported 40% generation speed improvement
- Community appreciation and recognition for the contribution
- Questions about compatibility with ROCm/Vulkan

**Discussion Highlights:** The community showed strong appreciation for the optimization work, with comments highlighting the author's frequent contributions and expressing interest in further improvements. There was also a question about whether the speedup would apply to ROCm/Vulkan in addition to CUDA.

---

## 8. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 289 | **Comments:** 34 | **Date:** 2025-12-12

**Summary:** The Reddit post discusses the feasibility and performance of running an LLM on a 3DS, sparking interest and curiosity among users about the potential of running AI on unconventional hardware. Key points include the exploration of running an LLM on a 3DS, comparisons to similar projects on other devices like the PS Vita and Wii, curiosity about performance improvements on a 'new' 3DS, the impressive nature of such projects, and speculation about the potential of AI in gaming and other applications. The discussion highlights the impressive nature of running LLMs on unconventional hardware like the 3DS, with users expressing curiosity and excitement about the potential performance improvements and applications of such technology.

---

## 9. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 243 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve throughput during text generation using Eagle3 speculative decoding. It is licensed for both commercial and non-commercial use.

**Key Points:**
- GPT-OSS-120B-Eagle3-throughput is an optimized speculative decoding module built on OpenAI's gpt-oss-120b base model.
- It uses NVIDIA’s Eagle3 speculative decoding approach to predict a single draft token efficiently.
- The model is licensed under the nvidia-open-model-license for commercial and non-commercial use.
- It is intended for applications like AI agents, chatbots, and retrieval-augmented generation (RAG) systems.
- The model is not supported in llama.cpp, as indicated by a stale feature request.

**Discussion Highlights:** The discussion includes requests for a derestricted version of the model and mentions of its potential benefits for CPU inference. There is also a note about the lack of support in llama.cpp and a humorous comment about waiting for a REAP EAGLE3 HERETIC MOE GGUF version.

---

## 10. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 237 | **Comments:** 77 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which users find unappealing and indicative of a decline in the company's direction.

**Key Points:**
- OpenAI's advertising shift from AI advancements to astrology ads
- Criticism of OpenAI's strategy and perceived decline
- Discussion on the profitability of targeting different user groups
- Suggestions for alternative advertising approaches
- Observation of OpenAI's change in messaging over a short period

**Discussion Highlights:** The discussion highlights a consensus that OpenAI's new advertising strategy is seen as a misstep, with users expressing disappointment and suggesting alternative approaches. There is also a focus on the profitability and targeting of different user demographics.

---

## 11. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 178 | **Comments:** 24 | **Date:** 2025-12-12

**Summary:** The post introduces Olmo 3.1 32B Think and Instruct models, two new 32-billion-parameter models optimized for deep reasoning and instruction following, respectively. The Think model excels in multi-step reasoning and code generation, while the Instruct model focuses on conversational fluency and tool-use capabilities.

**Key Points:**
- Olmo 3.1 32B Think and Instruct models are the newest additions to the Olmo family.
- The Think model is optimized for deep reasoning, math, logic, and code generation.
- The Instruct model is optimized for instruction following, conversational fluency, and tool-use capabilities.
- Both models are fully open-source and have received positive community feedback.
- The community anticipates future developments, such as Mixture of Experts (MOE) models.

**Discussion Highlights:** The community is enthusiastic about the new models, praising their open-source nature and improvements. There is anticipation for future developments like MOE models, and some users highlighted the educational value of the accompanying paper.

---

## 12. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 169 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that they share nearly identical sizes and architectures, with minor differences in expert configurations. The discussion highlights the open-source nature of these models and their adoption by various teams. Key points include: Mistral 3 Large and DeepSeek V3 have almost identical sizes (671B vs 673B); Mistral 3 Large uses the same architecture as DeepSeek V3/V3.1 but with adjusted expert sizes and counts; the Mistral team likely trained their model from scratch rather than fine-tuning DeepSeek V3; other models like Kimi K2 and Gigachat also use the DeepSeek V3 architecture; and the open-source community appreciates the reuse and adaptation of proven architectures. The discussion emphasizes the spirit of open source, where architectures are reused and adapted. Users appreciate the innovation within constraints and the practical benefits of proven architectures. Some comments highlight the efficiency and effectiveness of the DeepSeek V3 architecture, making it a popular choice among developers.

---

## 13. [Understanding the new router mode in llama cpp server](https://reddit.com/r/LocalLLaMA/comments/1pmc7lk/understanding_the_new_router_mode_in_llama_cpp/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 157 | **Comments:** 44 | **Date:** 2025-12-14

**Summary:** Router mode in llama cpp server allows managing multiple AI models simultaneously without restarting the server, similar to Ollama-like functionality. It enables loading/unloading models on demand and routing requests to the appropriate model, saving memory and simplifying model switching.

**Key Points:**
- Router mode enables managing multiple AI models without restarting the server.
- It allows loading/unloading models on demand and routing requests to the appropriate model.
- Saves memory and simplifies switching between models.
- Useful for testing multiple GGUF models, building local OpenAI-compatible APIs, and dynamic model switching.
- Discussion highlights include comparisons with llama-swap and requests for better VRAM management.

**Discussion Highlights:** The discussion includes comparisons with llama-swap, questions about specifying models to stay in memory, and requests for better VRAM management for multiple GPUs. Some users express familiarity with similar functionality in llama-swap.

---

## 14. [To Mistral and other lab employees: please test with community tools BEFORE releasing models](https://reddit.com/r/LocalLLaMA/comments/1pmgm2x/to_mistral_and_other_lab_employees_please_test/)

**Author:** u/dtdisapointingresult | **Upvotes:** 133 | **Comments:** 70 | **Date:** 2025-12-14

**Summary:** The Reddit post criticizes Mistral for releasing Devstral 2 without thorough testing with community tools, which led to issues like benchmark discrepancies and repetition loops. The author emphasizes the importance of testing with local tools to maintain reputation and user trust. Key points include the lack of testing with community tools, issues with benchmark discrepancies and repetition loops, and the influence of tech geeks in driving adoption. The discussion highlights mixed experiences with the model across different tools and a consensus on the importance of thorough testing with community tools before release.

---

## 15. [Qwen3-Next-80B-A3B-Thinking-GGUF has just been released on HuggingFace](https://reddit.com/r/LocalLLaMA/comments/1pmo0dn/qwen3next80ba3bthinkinggguf_has_just_been/)

**Author:** u/LegacyRemaster | **Upvotes:** 121 | **Comments:** 52 | **Date:** 2025-12-14

**Summary:** The Reddit post announces the release of Qwen3-Next-80B-A3B-Thinking-GGUF on HuggingFace, highlighting its impressive performance in a Tetris game implemented in a single HTML file. Users compare it favorably to other models like Devstral and discuss its capabilities and release timeline.

**Key Points:**
- Qwen3-Next-80B-A3B-Thinking-GGUF model released on HuggingFace
- Model excels in Tetris implementation within a single HTML file
- Performance compared favorably to Devstral
- Community discusses the model's capabilities and release timeline
- Questions about native tool calling support with llamacpp

**Discussion Highlights:** The community is highly impressed with the model's performance, particularly in iterative agentic coding tasks. Some users note the release timeline and discuss the model's potential applications, including its ability to handle classic games like Tetris. There are also technical discussions about tool calling support.

---

