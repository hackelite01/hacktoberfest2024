# Gemini-Powered Chatbot

A chatbot application built using React and Google's Gemini API. This project is designed for [Hacktoberfest](https://hacktoberfest.com/) contributions and aims to help developers and contributors build interactive chatbot systems.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Docker Setup](#docker-setup)
- [Contributing](#contributing)


## Introduction

The **Gemini-Powered Chatbot** leverages Google's generative AI APIs to create intelligent chatbot interactions. It is built using React on the front-end, with support for modern development workflows and Docker for containerized deployments. This project is open for contributions as part of Hacktoberfest 2024.

## Features

- **AI-powered Conversations**: Utilizes Google's Gemini API for generating responses.
- **Interactive Frontend**: Built using React for dynamic and smooth user experiences.
- **Containerized Deployment**: Docker support for easy deployment across environments.
- **Hacktoberfest Friendly**: Open for contributions and improvements.

## Tech Stack

- **Frontend**: React.js
- **Containerization**: Docker
- **Build Tools**: React Scripts, NPM

## Getting Started

Follow these steps to get the chatbot up and running on your local machine.

### Prerequisites

- Node.js (v20 or higher)
- NPM (or Yarn)
- Docker (for containerized setup)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sujaydeshpande/chatbot.git
   cd chatbot

2. Create the [.env] file and add following data:
    ```bash
    REACT_APP_API_KEY = #Gemini-API
3. Install dependencies:
    ```bash
    npm install

4. Start the development server:
    ```bash
    npm run dev

## Docker Setup
This project includes a Dockerfile for containerized deployments, allowing you to easily build and run the chatbot.

### Build Docker Image
* Run the following command to build the Docker image:
    ```bash
    docker build -t chatbot .

### Run Docker Container
* Once the image is built, run the container:
    ```bash
    docker run -p 3000:3000 chatbot

## Dockerfile
* Below is the content of the Dockerfile used for this project:
    ```dockerfile
    FROM node:20-alpine 

    WORKDIR /app

    COPY package*.json ./

    RUN npm install

    COPY . .

    EXPOSE 3000

    CMD ["npm", "run", "dev"]

## Contributing
Contributions are welcome! Whether it's fixing bugs, adding new features, or improving documentation, we appreciate your help. Follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit them 
    ```bash
    git commit -m 'Add some feature'
4. Push to the branch 
    ```bash 
    git push origin feature-branch
5. Open a pull request.