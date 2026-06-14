# FDA Adverse Events Analysis: Ibuprofen vs Acetaminophen

A data analysis project comparing side effects of two common painkillers using real-world FDA data.

## Why I did this
With my background in pharmacy, I wanted to clear up a common misconception that "paracetamol and ibuprofen are exactly the same." I wanted to use data analysis to prove that their actual side effects are different. Also, I wanted to show that drug data contains a lot of "noisy" symptoms (general reactions that happen with almost any drug).

## What I did
1. **Extracted data via API:** I think pulling exactly what I need through the openFDA API is much better and more efficient than downloading a massive 20M+ row dataset.
2. **Cleaned the data:** Removed non-clinical symptoms from the reactions list to get accurate results.
3. **Visualized the data:** Built charts to make the numbers easy to read and compare.
4. **Found hidden signals:** Compared unique serious reactions and found a severe side effect that remained unnoticed in the general noise.
<img width="1489" height="690" alt="png" src="https://github.com/user-attachments/assets/50955bf1-9595-49e2-82f0-bf726c7183db" />
What I found
- The noise is high: If you just look at the top reactions, both drugs look exactly the same (nausea, pain, fatigue). You have to dig deeper.
- Unique profiles: When I filtered for unique serious reactions, ibuprofen showed specific issues like urticaria. Acetaminophen data was actually heavily skewed by combination drugs (like when it's mixed with opioids), showing signs of dependence.
- Limitation: Basic counting isn't enough. Famous severe side effects (like liver issues for paracetamol) got completely lost in the shared "noise".

## Next Steps (WIP)
Right now, I am working on the next phase of this project:
- Adding PRR (Proportional Reporting Ratio) calculations to do proper statistical signal detection instead of just counting rows.
- Setting up a simple pipeline to automate the data extraction.

## Tech Stack
Python (pandas, matplotlib, requests), Jupyter Notebook.

