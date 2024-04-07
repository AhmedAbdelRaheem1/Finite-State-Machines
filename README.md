## Introduction to Finite State Machines (FSMs)

Finite state machines (FSMs) are mathematical models of computation, representing abstract machines that can exist in exactly one of a finite number of states at any given time. These machines transition from one state to another in response to inputs, a process known as a transition. An FSM is characterized by its states, initial state, and the inputs that trigger transitions.

## Applications of FSMs

Finite state machines (FSMs) have a wide range of applications across various domains, showcasing their versatility and efficiency. In natural language processing, FSMs are utilized for sentiment analysis, effectively classifying emotions based on textual data. In digital circuit design, FSMs are crucial for creating sequential logic circuits, such as the implementation of a 4-bit counter. Moreover, FSMs are indispensable in graph theory, aiding in the identification of circuits within interconnected systems. These applications highlight the broad utility of FSMs in addressing real-world problems, providing structured models for analyzing, designing, and comprehending complex systems across different fields.

## Mathematical Model of FSM

A deterministic finite-state machine (FSM) is represented as a quintuple, denoted as M(Σ, S, s0, δ, F), where:

- Σ: Input alphabet, a finite non-empty set of symbols.
- S: Set of states, a finite non-empty collection.
- s0: Initial state, an element of S.
- δ: State-transition function, δ: S × Σ → S.
- F: Set of final states, a (possibly empty) subset of S.

FSMs encompass two primary models: Mealy machines and Moore machines. In Mealy machines, the output depends on both current states and input symbols (ω: S × Σ → Γ), while in Moore machines, the output relies solely on states (ω: S → Γ). Additionally, in both deterministic and non-deterministic FSMs, it is customary to allow partial functions for δ(s, x), where not every combination of s ∈ S and x ∈ Σ needs to be defined. This flexibility enables FSMs to handle undefined transitions by signaling errors, enhancing their versatility in general state machine definitions.