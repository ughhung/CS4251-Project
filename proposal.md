Analysis of Datacenter Network Topologies for AI Training 

Hung Nguyen, Maria Cymbalyuk, Tai Wei Wu, Kritheesh Elangathir, Masih Ahmed 

CS 6250/4251 Networking II — Fall 2026 

 

Training large AI models requires many GPUs working together, which means those GPUs must repeatedly communicate with each other through operations such as AllReduce and AllToAll. As these clusters grow, the network connecting the GPUs can become a major performance bottleneck. This problem can already be seen in large-scale AI systems. In 2026, Meta described training its GEM foundation model across several thousand GPUs and explained that communication overhead was one of the factors reducing scaling efficiency. Meta uses a topology-aware training strategy that maps different types of communication onto different levels of a three-tier network based on the bandwidth available at each level [4]. This shows that the structure of the network can play an important role in how large-scale AI training is organized. Our project asks: How does the physical topology of a datacenter network affect distributed AI training performance when the other major system and network settings are controlled? To study this, we will use ASTRA-sim with its ns-3 network backend to run the same distributed-AI workloads across several different physical network topologies. These will include a fat-tree/Clos-style topology, a torus/ring-style topology, a hierarchical hybrid, and a custom topology designed by our team. During each comparison, we will keep the workload trace, number of simulated GPUs, logical topology, collective communication implementation, and comparable bandwidth and latency settings controlled. This will allow us to focus more directly on how the physical network topology affects performance. Our primary performance metric will be the total workload completion time. We will also examine flow completion time and available congestion or utilization measurements to better understand why certain topologies perform better or worse. We will test both AllReduce and AllToAll as separate controlled experiment families and, if feasible based on our baseline simulation results, extend the comparison to multiple GPU scales. 

Our project builds on previous research that has studied the relationship between network structure and distributed AI training. ASTRA-sim2.0 [1] is the simulation framework we will use and extend the original ASTRA-sim infrastructure to support more complex distributed training systems and network topologies. Prior work in [2] directly examines fat-tree/Clos and torus topologies for machine-learning collective communication, which is closely related to our research question. The paper finds that no single topology performs best in every situation, although Clos achieves better collective completion time in most cases evaluated. Rail-only [3] takes a different approach by redesigning the physical network around the communication patterns used during large language model training. The design reports network-cost reductions of 38–77% and power reductions of 37–75% while maintaining training performance. These studies show that network topology can have important effects on both the performance and design of large AI systems. Our project examines this same general problem through our own controlled simulations using ASTRA-sim and ns-3 across several physical topologies and communication workloads, with a possible extension to multiple GPU scales. Instead of only determining which topology finishes the workload fastest, we also want to examine what happens inside the network and explain why performance differences occur. 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

References 

[1] W. Won, T. Heo, S. Rashidi, S. Sridharan, S. Srinivasan, and T. Krishna, "ASTRA-sim2.0: Modeling hierarchical networks and disaggregated systems for large-model training at scale," in Proc. IEEE Int. Symp. Performance Analysis of Systems and Software (ISPASS), Raleigh, NC, USA, 2023, pp. 283–294. [Online]. Available: https://arxiv.org/abs/2303.14006 

[2] S. McClure et al., "On topology's role in ML training performance," arXiv preprint arXiv:2608.01707, Aug. 2026. [Online]. Available: https://arxiv.org/abs/2608.01707 

[3] W. Wang, M. Ghobadi, K. Shakeri, Y. Zhang, and N. Hasani, "Rail-only: A low-cost high-performance network for training LLMs with trillion parameters," in Proc. IEEE Symp. High-Performance Interconnects (HOTI), 2024, pp. 1–10. [Online]. Available: https://arxiv.org/abs/2307.12169 

[4] D. Liu et al., "Training GEM at LLM scale: Meta's ads recommendation foundation model," Engineering at Meta, Aug. 3, 2026. [Online]. Available: https://engineering.fb.com/2026/08/03/ml-applications/training-gem-at-llm-scale-meta-ads-recommendation-foundation-model/ 

 