-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "clean_data" (
    "id" serial   NOT NULL,
    "age" float   NOT NULL,
    "current_smoker" int   NOT NULL,
    "stroke" int   NOT NULL,
    "hypertension" int   NOT NULL,
    "bmi" float   NOT NULL,
    "avg_glucose_level" int   NOT NULL,
    "gender" varchar  NOT NULL,
    CONSTRAINT "pk_clean_data" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "scaled_data" (
    "id" serial   NOT NULL,
    "clean_data_id" int   NOT NULL,
    "age" float   NOT NULL,
    "current_smoker" int   NOT NULL,
    "stroke" int   NOT NULL,
    "hypertension" int   NOT NULL,
    "bmi" float   NOT NULL,
    "avg_glucose_level" int   NOT NULL,
    "gender_Female" int   NOT NULL,
    "gender_Male" int   NOT NULL,
    "gender_Other" int   NOT NULL,
    CONSTRAINT "pk_scaled_data" PRIMARY KEY (
        "id"
     )
);

ALTER TABLE "scaled_data" ADD CONSTRAINT "fk_scaled_data_clean_data_id" FOREIGN KEY("clean_data_id")
REFERENCES "clean_data" ("id");

