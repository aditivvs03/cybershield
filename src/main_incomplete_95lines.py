from dotenv import load_dotenv

load_dotenv(override=True)



import os

import csv

import json

import re

from datetime import datetime

import numpy as np

import pandas as pd

import joblib

import uvicorn



from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from urllib.parse import urlparse



import google.generativeai as genai



# ── Init app ──

app = FastAPI(

    title="CyberShield API",

    description="AI-Based Cyber Threat Detection System",

    version="1.1.0"

)



# ── CORS — allows Chrome extension and React to call this API ──

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_methods=["*"],

    allow_headers=["*"],

)



# ── Load models ──

print("Loading models...")

rf_model  = joblib.load("../models/random_forest.pkl")

print("MODEL EXPECTS:", list(rf_model.feature_names_in_))

xgb_model = joblib.load("../models/xgboost.pkl")

print("RF classes:", rf_model.classes_)

print("XGB classes:", xgb_model.classes_)



with open("../models/ensemble_config.json") as f:

    config = json.load(f)



with open("../models/metrics.json") as f:

    metrics = json.load(f)
