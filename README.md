<a name="readme-top"></a>

<div align="center">
  <img src="public/logo-dark.png" alt="logo" width="140"  height="auto" />

  <br/>
</div>

# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Login](#login)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [🤝 Contributing](#contributing)
- [⭐️ Show your support](#support)
- [📝 License](#license)

# 📖 HR Pulse Backend <a name="about-project"></a>

HR Pulse Backend is an HR analytics and skill extraction platform designed to streamline human resource management processes. It leverages AI and machine learning to extract skills from job descriptions and provide intelligent insights for better decision-making.

## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

  <ul>
    <li><a href="https://fastapi.tiangolo.com/">FastAPI</a></li>
    <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a></li>
    <li><a href="https://www.postgresql.org/">PostgreSQL</a></li>
    <li><a href="https://azure.microsoft.com/en-us/services/cognitive-services/text-analytics/">Azure AI Text Analytics</a></li>
    <li><a href="https://scikit-learn.org/">Scikit-learn & XGBoost</a></li>
  </ul>

### Key Features <a name="key-features"></a>

- **AI Skill Extraction**: Automatic extraction of professional skills from text using Azure AI.
- **Predictive Analytics**: Machine learning models for HR-related predictions and data analysis.
- **RESTful API**: Robust and documented endpoints for seamless frontend integration.
- **Secure Authentication**: JWT-based user authentication and role management.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Live Demo <a name="live-demo"></a>

- [Live Demo Link](https://hr-pulse-api.example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Setup

Clone this repository to your desired folder:

```sh
  git clone https://github.com/codehass/HR-Pulse.git
  cd HR-Pulse
```

### Install

Install dependencies using `uv` or `pip`:

```sh
  uv sync
```

Create a `.env` file and add your environment variables. You can copy `.env.example` as a template.

```sh
  cp .env.example .env
```

### Usage

To run the project in development mode, execute the following command:

```sh
  fastapi dev app/main.py
```

### Login

You can access the interactive API documentation at:
- Swagger: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 👥 Author <a name="authors"></a>

👤 **Hassan El Ouardy**

- GitHub: [@codehass](https://github.com/codehass)
- Twitter: [@hassanelourdy](https://twitter.com/hassanelourdy)
- LinkedIn: [@hassanelourdy](https://www.linkedin.com/in/hassanelouardy/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🔭 Future Features <a name="future-features"></a>

- **Advanced ML Models**: Integration of more sophisticated NLP models for better accuracy.
- **Real-time Collaboration**: WebSocket support for real-time HR data updates.
- **Automated Resume Screening**: Direct parsing and analysis of candidate resumes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🤝 Contributing <a name="contributing"></a>

Contributions, issues, and feature requests are welcome!

Feel free to check the [issues page](https://github.com/codehass/HR-Pulse/issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## ⭐️ Show your support <a name="support"></a>

If you like this project, give it a star! Your support helps us continue developing tools for better HR management.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 📝 License <a name="license"></a>

This project is [MIT](./MIT.md) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
