# Nicholas Shead s342738 HIT137 Assignment 1

# Multimodal models have begun to take hold within the healthcare sector, allowing people to integrate diverse data sources and gain deeper insights into patient health. 
# This type of modelling combines information from text, imagery and video, which can potentially enhance diagnostics, personalise treatment, and improve patient outcomes. 
# By integrating frameworks within the Python language, various tools can be rapidly employed to understand and gain insight from large datasets and then use this to effectively provide treatment.

# The World Health Organisation has released guidance on the ethics and guidance of AI in the health.  
# Broader societal risks associated with the growing use of LMM’s include the fact that LMM’s are often developed and deployed by large technology companies, due partly to the significant computing, data, human and financial resource required for development of LMM’s (WHO, 2024).  
# LMM’s have the ability to enhance disease prediction, personalize treatment plans, and improve patient monitoring.  
# As they gain use in the broader health care areas, errors and misuse are of course inevitable with any new technology.  

# Their applications include diagnosis, drug discovery, medical education, and scientific research.  
# LMM’s can integrate information from medical imagery and collate this with clinical notes.  
# Early detection of diseases by looking for pattern recognition from the onset by detecting subtle abnormalities.  
# They are also beneficial for drug discovery and development, identifying potential candidates more effectively.  
# Personalised treatments plans can utilise real time sensor readings, tailoring the treatment efficiently.

# Multimodal models can inherit biases from training data. 
# Ensuring their fairness and addressing bias is crucial. 
# LMM’s data can be sensitive (e.g., medical records, images, video), so protecting privacy is essential.  
# Unauthorised access or misuse of personal information must be prevented like all sensitive data must be.  
# Developers of the models must be held accountable with data to the same level as medical practitioners.

# It is beneficial to be aware of the potential pitfalls associated with the use of AI, such as automation bias (Brown, 2023).  
# Health care practitioners can over rely on such systems without being critical as AI tools can be flawed.  
# Human judgment should complement AI decisions, as models potentially contain biased or an incomplete data set.  
# Practitioners must be able to understand the basics of how they systems such as LMM’s are constructed, including their limitations.  
# Patients require transparent decision making when formulating their treatment. 

# PyHealth is an open-source Python toolbox specifically designed for developing predictive models on healthcare data. 
# It covers various predictive models on healthcare data (Zhao et al, 2021), allowing users such as computer science researches and data scientists to conduct complex machine learning with basic coding from within Python.  
# It encompasses many predictive health algorithms, with access to the typical underlying Python libraries such as Scikit-learn, TensorFlow, NLTK and OpenCV.

# For python to interpret the data sets, the data requires pre-processing based on its data type.  
# Various methods can be employed such as:
# •	natural language processing (NLP) to extract clinical concepts from medical notes.
# •	convolutional neural networks (CNNs) to extract visual features of imagery
# •	recurrent neural networks (RNNs) for temporal patterns of time sequenced data.
# The data also requires normalisation and standardisation to ensure a fair comparison by normalising data across modalities.

# Multimodal models have the potential to revolutionise healthcare. 
# As Python tools evolve and their application can be expanded, information and thus wisdom can be gained where previously it was unknown.  
# Indeed, there are concerns with privacy and data security as this type of information can be valuable.  
# Python and its libraries provide a powerful tool for rapid prototyping and data exploration when developing data science pipelines (McNamara et al, 2017).

# References:
# Brown, C., Nazeer, R., Gibbs, A., Le Page, P., & Mitchell, A. R. (2023). Breaking Bias: The Role of Artificial Intelligence in Improving Clinical Decision-Making. Cureus, 15(3), e36415. https://doi.org/10.7759/cureus.36415
# Hashimoto, N., Hanada, H., Miyoshi, H., Nagaishi, M., Sato, K., Hontani, H., Ohshima, K., & Takeuchi, I. (2023). Multimodal Gated Mixture of Experts Using Whole Slide Image and Flow Cytometry for Multiple Instance Learning Classification of Lymphoma. Journal of pathology informatics, 15, 100359. https://doi.org/10.1016/j.jpi.2023.100359
# Lee, G., Kang, B., Nho, K., Sohn, K. A., & Kim, D. (2019). MildInt: Deep Learning-Based Multimodal Longitudinal Data Integration Framework. Frontiers in genetics, 10, 617. https://doi.org/10.3389/fgene.2019.00617
# McNamara, Q., De La Vega, A., & Yarkoni, T. (2017, August). Developing a comprehensive framework for multimodal feature extraction. In Proceedings of the 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (pp. 1567-1574).
# World Health Organization. (n.d.). Ethics and governance of Artificial Intelligence for Health. World Health Organization. https://www.who.int/publications/i/item/9789240029200
# Zhao, Y., Qiao, Z., Xiao, C., Glass, L., & Sun, J. (2021). Pyhealth: A python library for health predictive models. arXiv preprint arXiv:2101.04209.