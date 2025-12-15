# r/LocalLLaMA Reading Digest

**Period:** 2025-12-11 to 2025-12-14
**Posts Summarized:** 15
**Total Posts Analyzed:** 16

---

## 1. [Someone from NVIDIA made a big mistake and uploaded the parent folder of their upcoming model on Hugging Face](https://reddit.com/r/LocalLLaMA/comments/1pkpxss/someone_from_nvidia_made_a_big_mistake_and/)

**Author:** u/Nunki08 | **Upvotes:** 1278 | **Comments:** 149 | **Date:** 2025-12-12

**Summary:** A NVIDIA employee accidentally uploaded the parent folder of an upcoming model on Hugging Face, sparking interest and urgency among users to save the content before potential removal.

**Key Points:**
- NVIDIA's accidental upload of an upcoming model's parent folder on Hugging Face
- Users expressing urgency to save the content before it gets taken down
- Mentions of specific models like Nano and 30B-A3B
- Positive feedback on the Nemotron lineup and related projects
- Concerns about potential censorship of the uploaded content

**Discussion Highlights:** The discussion highlights a sense of urgency among users to preserve the accidentally uploaded content, with mentions of specific models and positive feedback on related projects. There is also a consensus on the potential for censorship and the need to act quickly.

---

## 2. [Training an LLM only on 1800s London texts - 90GB dataset](https://reddit.com/r/LocalLLaMA/comments/1pkpsee/training_an_llm_only_on_1800s_london_texts_90gb/)

**Author:** u/Remarkable-Trick-177 | **Upvotes:** 657 | **Comments:** 71 | **Date:** 2025-12-12

**Summary:** The post discusses the TimeCapsuleLLM project, which involves training an LLM on a 90GB dataset of 1800-1875 London texts. The author has conducted a bias report and trained a small evaluation model to assess the dataset before scaling up.

**Key Points:**
- The dataset consists of 90GB with 135,000 documents from the Internet Archive.
- A bias report covering temporal, gender/pronoun, and geographic bias has been generated.
- A small evaluation model (300M parameters) was trained on a 15GB subset to evaluate the dataset.
- The community appreciates the detailed work and suggests considering MoE for better compute efficiency.
- The project aims to study historical texts despite inherent biases.

**Discussion Highlights:** The community shows strong support for the project, with suggestions for improvement such as using Mixture of Experts (MoE) for better compute efficiency. There is also interest in the methodology and progress of the project.

---

## 3. [8x RTX Pro 6000 server complete](https://reddit.com/r/LocalLLaMA/comments/1plwgun/8x_rtx_pro_6000_server_complete/)

**Author:** u/koushd | **Upvotes:** 594 | **Comments:** 262 | **Date:** 2025-12-13

**Summary:** The post details a user's journey upgrading their GPU server from a single 3080 to an 8x RTX Pro 6000 setup with a Threadripper PRO 9955WX CPU and 384 GB RAM, facing challenges like overheating and power management.

**Key Points:**
- 8x RTX Pro 6000 GPUs with 768 GB VRAM
- Threadripper PRO 9955WX CPU and 384 GB RAM
- Challenges with overheating and IOMMU addressing
- Community reactions and technical advice in comments

**Discussion Highlights:** The community expressed awe at the setup, with some critiquing the hardware placement and others sharing similar experiences and advice.

---

## 4. [OpenAI's flagship model, ChatGPT-5.2 Thinking, ranks  most censored AI on Sansa benchmark.](https://reddit.com/r/LocalLLaMA/comments/1plnuqu/openais_flagship_model_chatgpt52_thinking_ranks/)

**Author:** u/Difficult-Cap-7527 | **Upvotes:** 588 | **Comments:** 105 | **Date:** 2025-12-13

**Summary:** The Reddit post discusses OpenAI's ChatGPT-5.2 model being ranked as the most censored AI on the Sansa benchmark, with users reporting issues in follow-up questions, research capabilities, and processing clinical notes.

**Key Points:**
- ChatGPT-5.2 is ranked as the most censored AI on the Sansa benchmark.
- Users report the model performs poorly on follow-up questions and research tasks compared to previous versions.
- Difficulties in processing made-up clinical notes for evaluation purposes.
- Questions raised about the testing criteria used in the benchmark.
- Observations that Gemini is less censored than other models, including Mistral.

**Discussion Highlights:** The discussion highlights concerns about the model's performance degradation in specific tasks and questions about the benchmark's testing criteria. Users express frustration with the model's limitations in handling certain types of content.

---

## 5. [The new monster-server](https://reddit.com/r/LocalLLaMA/comments/1pl0ojb/the_new_monsterserver/)

**Author:** u/eribob | **Upvotes:** 571 | **Comments:** 116 | **Date:** 2025-12-12

**Summary:** The Reddit post details a user's upgraded 'Monster Server' setup, featuring a Ryzen 3950x CPU, three GPUs (2x RTX 3090 and 1x RTX 4090), 128GB RAM, and extensive storage. The user runs local LLMs like GPT-OSS-120B for research and coding, leveraging high-speed 10GBe networking. Key points include the hardware setup, usage of GPT-OSS-120B, and discussion highlights such as nostalgia for early tech forums, questions about the user's location for affordable high-speed internet, and technical feedback on GPU parallelism efficiency. Users also expressed interest in heat management and the second PSU setup.

---

## 6. [New in llama.cpp: Live Model Switching](https://reddit.com/r/LocalLLaMA/comments/1pk0ubn/new_in_llamacpp_live_model_switching/)

**Author:** u/paf1138 | **Upvotes:** 456 | **Comments:** 83 | **Date:** 2025-12-11

**Summary:** The Reddit post announces a new feature in llama.cpp called 'Live Model Switching'. The community response highlights its popularity, mentions related tools like 'llamaswap', and expresses appreciation for recent UX improvements.

**Key Points:**
- New feature: Live Model Switching in llama.cpp
- Post gained significant traction with 456 upvotes
- Community mentions tools like 'llamaswap' and UX improvements
- User expresses intention to switch from 'ollama'
- Post was featured on Discord and received special recognition

**Discussion Highlights:** The discussion reflects positive sentiment around the new feature, with users appreciating the progress in UX and expressing interest in switching from alternative tools like 'ollama'. The post's popularity is noted, and related tools like 'llamaswap' are mentioned in the conversation.

---

## 7. [Mistral’s Vibe CLI now supports a 200K token context window (previously 100K)](https://reddit.com/r/LocalLLaMA/comments/1pjw7rj/mistrals_vibe_cli_now_supports_a_200k_token/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 434 | **Comments:** 36 | **Date:** 2025-12-11

**Summary:** Mistral’s Vibe CLI has doubled its context window from 100K to 200K tokens, a change achieved with a simple configuration update. The community has reacted positively, though some question the practical usefulness of such large context windows.

**Key Points:**
- Context window increased from 100K to 200K tokens
- Change was a simple configuration update (auto_compact_threshold: 100_000 → 200_000)
- Community appreciates the update but debates its practical utility
- Some users note models often struggle with context beyond 100K tokens
- Update allows for summarizing longer sessions, even if performance may degrade

**Discussion Highlights:** The community celebrated the update, with one user highlighting the simplicity of the change (a single line of code). However, discussions also revealed skepticism about the practical benefits of a 200K context window, with some users noting that models often struggle with context beyond 100K tokens. The consensus leans toward appreciating the flexibility for edge cases like session summarization.

---

## 8. [What is the smartest uncensored nsfw LLM you can run with 12GB VRAM and 32GB RAM?](https://reddit.com/r/LocalLLaMA/comments/1pkidf6/what_is_the_smartest_uncensored_nsfw_llm_you_can/)

**Author:** u/Dex921 | **Upvotes:** 401 | **Comments:** 146 | **Date:** 2025-12-11

**Summary:** The post asks for recommendations on the smartest uncensored NSFW LLM that can be run with 12GB VRAM and 32GB RAM, including both local and closed-source options.

**Key Points:**
- The post allows for both local and closed-source LLM recommendations.
- TheDrummer_Cydonia-24B is mentioned as a truly uncensored local model.
- Qwen3 32B is noted for good NSFW roleplay results on a laptop with RTX3070 and 32GB RAM.
- The discussion highlights a focus on uncensored and NSFW capabilities.

**Discussion Highlights:** The discussion primarily focuses on uncensored and NSFW capabilities of LLMs, with specific recommendations for local models like TheDrummer_Cydonia-24B and Qwen3 32B. There is a consensus on the importance of uncensored models for NSFW use cases.

---

## 9. [Qwen3 Next generation optimization](https://reddit.com/r/LocalLLaMA/comments/1plng6f/qwen3_next_generation_optimization/)

**Author:** u/ilintar | **Upvotes:** 352 | **Comments:** 39 | **Date:** 2025-12-13

**Summary:** The post discusses optimizations made to Qwen3, specifically an autoregressive delta net computation that improves generation speed by 40%. The author invites others to test the optimizations and share their results.

**Key Points:**
- Optimized autoregressive delta net computation for Qwen3
- 40% generation speed improvement reported
- Optimizations remove unnecessary reshapes and computations
- Community encouraged to test and provide feedback
- Discussion includes questions about compatibility with ROCm/Vulkan

**Discussion Highlights:** The community shows strong appreciation for the optimization work, with comments highlighting the author's frequent contributions and expressing interest in further improvements. There is also a question about whether the speedup applies to ROCm/Vulkan in addition to CUDA.

---

## 10. [Running an LLM on a 3DS](https://reddit.com/r/LocalLLaMA/comments/1pl4njj/running_an_llm_on_a_3ds/)

**Author:** u/vreab | **Upvotes:** 283 | **Comments:** 31 | **Date:** 2025-12-12

**Summary:** The post discusses the feasibility and performance of running an LLM on a Nintendo 3DS, drawing comparisons to similar projects on platforms like the PS Vita and Wii. Users express admiration for the technical achievement and curiosity about potential performance improvements on newer hardware.

**Key Points:**
- Running an LLM on a 3DS is technically feasible, as demonstrated by similar projects on PS Vita and Wii.
- Users are impressed by the technical achievement and potential applications.
- There is curiosity about whether a 'new' 3DS would offer significant performance improvements.
- Comparisons are drawn to other unconventional platforms like a Samsung fridge running Doom.

**Discussion Highlights:** The discussion highlights a mix of admiration for the technical feat and curiosity about the practical implications. Users are particularly interested in how such projects push the boundaries of what is possible on older or unconventional hardware. There is also a lighthearted tone, with references to other unconventional tech projects like running Doom on a fridge.

---

## 11. [NVIDIA gpt-oss-120b Eagle Throughput model](https://reddit.com/r/LocalLLaMA/comments/1plewrk/nvidia_gptoss120b_eagle_throughput_model/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 240 | **Comments:** 53 | **Date:** 2025-12-13

**Summary:** The post discusses NVIDIA's GPT-OSS-120B-Eagle3-throughput model, an optimized speculative decoding module designed to improve text generation throughput using Eagle3 speculative decoding. It is licensed for both commercial and non-commercial use. Key points include its use of NVIDIA’s Eagle3 speculative decoding approach, licensing under nvidia-open-model-license, and its intended use in AI agents, chatbots, and RAG systems. The discussion highlights include requests for a derestricted version, questions about CPU inference speed improvements, and mentions of the model's lack of support in llama.cpp.

---

## 12. [This is how open ai is advertising them selfs on reddit…. They are doomed](https://reddit.com/r/LocalLLaMA/comments/1plcrg8/this_is_how_open_ai_is_advertising_them_selfs_on/)

**Author:** u/ThinkExtension2328 | **Upvotes:** 233 | **Comments:** 76 | **Date:** 2025-12-12

**Summary:** The Reddit post criticizes OpenAI's advertising strategy, highlighting a shift from promoting advanced AI to using astrology ads, which users find unappealing and indicative of a decline in the company's direction.

**Key Points:**
- OpenAI's advertising shift from AI advancements to astrology ads
- Criticism of OpenAI's strategy and perceived decline
- Discussion on the profitability of targeting different user groups
- Suggestions for alternative advertising approaches
- Observations on the rapid change in OpenAI's messaging

**Discussion Highlights:** Users express disappointment and criticism towards OpenAI's new advertising approach, suggesting it may not resonate with their target audience and indicating a perceived fall from grace.

---

## 13. [Agentic Local AI on CPU = Mistral Vibe + Granite-4-h-1b](https://reddit.com/r/LocalLLaMA/comments/1pkdkjo/agentic_local_ai_on_cpu_mistral_vibe_granite4h1b/)

**Author:** u/PotentialFunny7143 | **Upvotes:** 231 | **Comments:** 40 | **Date:** 2025-12-11

**Summary:** The post discusses the effectiveness of using Mistral Vibe and Granite-4-h-1b for agentic local AI on CPU, highlighting its capabilities and performance.

**Key Points:**
- Mistral Vibe and Granite-4-h-1b are effective for local AI on CPU.
- Performance metrics and hardware requirements are of interest to users.
- Comparisons with other models like Cline and open code are discussed.
- Users are curious about the upper boundary capabilities and resource consumption.

**Discussion Highlights:** Users are interested in performance metrics, hardware requirements, and comparisons with other models. There is a focus on understanding the capabilities and resource consumption of Mistral Vibe and Granite-4-h-1b.

---

## 14. [Olmo 3.1 32B Think &amp; Instruct: New Additions to the Olmo Model Family](https://reddit.com/r/LocalLLaMA/comments/1pky5u4/olmo_31_32b_think_instruct_new_additions_to_the/)

**Author:** u/Dear-Success-1441 | **Upvotes:** 175 | **Comments:** 24 | **Date:** 2025-12-12

**Summary:** The post introduces Olmo 3.1 32B Think and Instruct models, each optimized for different use cases: deep reasoning and instruction following, respectively. The community response highlights enthusiasm for the open-source models and their educational value.

**Key Points:**
- Olmo 3.1 32B Think model excels in deep reasoning, math, logic, and code generation.
- Olmo 3.1 32B Instruct model is optimized for instruction following and conversational fluency.
- Community praises the open-source nature and educational value of the models.
- Anticipation for future MOE models and weekend experimentation.

**Discussion Highlights:** The discussion reflects positive sentiment towards the new models, with users appreciating their open-source nature and educational value. There is also anticipation for future developments and experimentation with the models.

---

## 15. [Mistral 3 Large is DeepSeek V3!?](https://reddit.com/r/LocalLLaMA/comments/1plpc6h/mistral_3_large_is_deepseek_v3/)

**Author:** u/seraschka | **Upvotes:** 164 | **Comments:** 33 | **Date:** 2025-12-13

**Summary:** The post discusses the architectural similarities between Mistral 3 Large and DeepSeek V3, noting that Mistral 3 Large uses the same architecture as DeepSeek V3 but with adjustments to expert size and count. The discussion highlights the open-source nature of these models and the adoption of DeepSeek V3 architecture by multiple teams.

**Key Points:**
- Mistral 3 Large and DeepSeek V3 have nearly identical sizes (671B vs. 673B).
- Mistral 3 Large uses the same architecture as DeepSeek V3 but with larger experts and fewer in number.
- The Mistral team likely trained Mistral 3 from scratch rather than fine-tuning DeepSeek V3.
- Multiple models, including Kimi K2 and Gigachat, are based on the DeepSeek V3 architecture.
- The open-source community appreciates the reuse and adaptation of successful architectures.

**Discussion Highlights:** The discussion emphasizes the spirit of open source, with multiple teams adopting and adapting the DeepSeek V3 architecture. Users note that while Mistral 3 Large reuses this architecture, it introduces innovations like multimodal capabilities. The consensus is that the DeepSeek V3 architecture is effective and widely adopted due to its proven performance.

---

