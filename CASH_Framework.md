graph TB
    subgraph "CASH Framework"
        direction TB
        CEE[Confidentiality<br>Chaotic Entropic Expansion]
        AOW[Reliability<br>Affine One-Wayness]
        SH[Opposability<br>Semantic Holder]
    end

    subgraph "AOW Core Components"
        direction TB
        FF[Finite Field Arithmetic]
        AIIP[Affine Iterated Inversion Problem]
        POLY[Polynomial Iteration]
    end

    subgraph "SH Core Components"
        direction TB
        AE[Algebraic Extraction]
        SM[Semantic Mapping φ]
        VE[Verifiable Explanation]
        LC[Legal Context]
    end

    subgraph "CEE Core Components"
        direction TB
        CE[Chaotic Expansion]
        EP[Entropy Preservation]
        VC[Verifiable Computation]
    end

    subgraph "Security Foundations"
        direction TB
        MQ[MQ Problem Hardness]
        HCDLP[High-Genus HCDLP]
        STARK[STARK Proof System]
        QRP[Quantum Resistance]
    end

    subgraph "Applications"
        direction TB
        LSC[Legal Smart Contracts]
        RC[Regulatory Compliance]
        DEA[Digital Evidence Authentication]
        BFT[Byzantine Fault Tolerance]
        DS[Distributed Synchronization]
        VDF[Verifiable Delay Functions]
    end

    CASH --> AOW
    CASH --> CEE
    CASH --> SH
    
    AOW --> FF
    AOW --> AIIP
    AOW --> POLY
    
    SH --> AE
    SH --> SM
    SH --> VE
    SH --> LC
    
    CEE --> CE
    CEE --> EP
    CEE --> VC
    
    AIIP --> MQ
    AIIP --> HCDLP
    VE --> STARK
    CEE --> QRP
    
    AOW --> BFT
    AOW --> DS
    AOW --> VDF
    
    SH --> LSC
    SH --> RC
    SH --> DEA

    classDef cash fill:#e1f5fe
    classDef aow fill:#f3e5f5
    classDef sh fill:#fff3e0
    classDef cee fill:#e8f5e8
    classDef security fill:#ffebee
    classDef apps fill:#f5f5f5
    
    class CEE,CEE,AOW,SH cash
    class FF,AIIP,POLY aow
    class AE,SM,VE,LC sh
    class CE,EP,VC cee
    class MQ,HCDLP,STARK,QRP security
    class LSC,RC,DEA,BFT,DS,VDF apps