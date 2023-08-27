# Multi-Label CS Keyword Prediction 

![Search Image](https://github.com/NifulIslam/Multilabel-Keyword-Prediction/blob/master/images/search.png)

This project involves scraping data from IEEE Xplore specifically in the field of computer science (more than 50K data was scrapped). The collected data is used to train a multi-label (510 classes) keyword prediction model. The model is trained using two different Hugging Face transformer architectures, namely DistilRoBERTa and DistilBERT. The training results for both models are as follows:

| Model       | Training Loss | Validation Loss | Training Accuracy <br> (Multi) |
|-------------|---------------|-----------------|-------------------|
| DistilRoBERTa | 0.003506      | 0.004463         | 0.998828              |
| DistilBERT | 0.005306      | 0.004990         | 0.998778              |

After training, the model is compressed using ONNX. The model has 0.96 micro F1-score and 0.41 macro F1-score. The compressed model is deployed on Hugging Face's model repository, and you can access it through this link: [Hugging Face Deployment](https://huggingface.co/spaces/NifulIslam/IEEE-Keyword-Prediction).

## Model Deployment

The deployed model is also integrated into a functional website hosted on Render. You can try out the model and see it in action through the following link: [Render Deployment](https://multilabel-keyword-prediction.onrender.com).

Here are some images to give you a glimpse of the deployed interfaces:

**Hugging Face Deployment Interface:**
![Hugging Face Interface](https://github.com/NifulIslam/Multilabel-Keyword-Prediction/blob/master/images/huggingface-interface.png)

**Final Deployed Website:**
![Website - Home](https://github.com/NifulIslam/Multilabel-Keyword-Prediction/blob/master/images/deploy-1.png)
![Website - Result](https://github.com/NifulIslam/Multilabel-Keyword-Prediction/blob/master/images/deploy-2.png)

This project allows users to input text and receive predicted keywords related to the field of machine learning. The website provides an intuitive interface to interact with the model, making it easier to extract relevant keywords from input text.
