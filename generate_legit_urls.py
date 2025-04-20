import pandas as pd
from utils.feature_extractor import extract_features

# ✅ List of legitimate URLs
urls = [
    "https://gems.phoenixclassroom.com/Account/login",
    "https://accounts.google.com/signin/v2/identifier",
    "https://elearn.lpu.in/Login.aspx",
    "https://learning.manipaldubai.com/d2l/home/10896"
]

# ✅ Extract features for each URL and mark as 'legitimate'
data = []
for url in urls:
    features_df = extract_features(url)
    if not features_df.empty:
        features_df["status"] = 0  # 0 = legitimate
        data.append(features_df)

# ✅ Combine all into one DataFrame
final_df = pd.concat(data, ignore_index=True)

# ✅ Save to CSV
final_df.to_csv("legitimate_samples.csv", index=False)
print("✅ legitimate_samples.csv generated!")
