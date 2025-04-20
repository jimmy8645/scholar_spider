# scholar_spider

A Scrapy-based project to scrape Google Scholar search results, compute a legitimacy score for each paper based on citation counts normalized by publication age, and generate a JSON report.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Navigate to the project root:

   ```bash
   cd books
   ```
2. Run the spider with your search query:

   ```bash
   scrapy crawl google_scholar -a query="your search terms"
   ```

3. The report will be saved to `reports/scholar_report.json` in the project root.

## Project Structure

```
books/
├── books/
│   ├── items.py        # Define GoogleScholarItem fields
│   ├── pipelines.py    # Compute legitimacy_score pipeline
│   ├── settings.py     # Configure pipelines, feeds, and crawling behavior
│   └── spiders/
│       └── google_scholar.py  # Spider for scraping Google Scholar
├── reports/            # Output directory for JSON report
└── scrapy.cfg          # Scrapy project configuration
