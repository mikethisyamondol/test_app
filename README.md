[![prod build](https://github.com/mikethisyamondol/test_app/actions/workflows/main.yml/badge.svg)](https://github.com/mikethisyamondol/test_app/actions/workflows/main.yml)
[![dev build](https://github.com/mikethisyamondol/test_app/actions/workflows/dev.yml/badge.svg)](https://github.com/mikethisyamondol/test_app/actions/workflows/dev.yml)

# Skeleton App with GCP

This app was built as a skeleton or scaffolding for future MLOps projects where the CI/CD pipeline and build/deploy infrastructure can be carried over relatively easily as long as it's hosted on Google Cloud Platform (GCP) specifically on Google App Engine. This microservice is built using FastAPI and currently has a roberta-base question answering model using the SQuAD2.0 dataset from Hugging Face (https://huggingface.co/deepset/roberta-base-squad2) plugged in for functionality but can be swapped out with any ML model. 

# Set Up

This repository contains two branches: main (prod) and dev, which are associated to different yaml files within .github/workflows that dictate the environment build and the deployment to Google App Engine via GitHub Actions. The statuses of each environment can be seen in the status badges above labeled "prod build" for the production environment and "dev build" for the development environment. Each environment is associated with different projects within GCP and thus produces separate app URLs to work in. The best practice is to develop within the development environment in the dev branch, and once QAed, can be merged into the main brance via Pull Request.

For this particular example, the roberta-base question answering model using the SQuAD2.0 dataset accepts two parameters: question and context which are inputs for the question answering model. We can use Swagger UI to test out the API in a user friendly fashion by adding "/docs" to the end of the app URL. 

<img width="1387" alt="Screen Shot 2022-06-01 at 9 02 08 AM" src="https://user-images.githubusercontent.com/12674202/171489675-c523ffb8-bbcb-4f39-8fc7-a300355aad56.png">

Once executed, the app will return a JSON object with the answer, the start and end index of the answer, and the score which how confident the model is of the answer.

<img width="1383" alt="Screen Shot 2022-06-01 at 9 02 28 AM" src="https://user-images.githubusercontent.com/12674202/171489978-77e2788c-5c31-4f06-9b0d-d54b6e5537dc.png">


