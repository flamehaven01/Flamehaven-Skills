# Examples

**Scenario:** SaaS product launch, monitor first 48 hours

**Execution:**

1. **EmotionFlowLLM Analysis:**
   ```python
   t=0h: {'joy': 0.72, 'anticipation': 0.65, 'trust': 0.58}  # Launch excitement
   t=12h: {'joy': 0.55, 'surprise': 0.42, 'neutral': 0.38}  # Initial usage
   t=24h: {'anger': 0.48, 'frustration': 0.52, 'sadness': 0.31}  # Bug discovered
   t=36h: {'trust': 0.41, 'anticipation': 0.38, 'neutral': 0.45}  # Fix announced
   t=48h: {'joy': 0.62, 'trust': 0.68, 'satisfaction': 0.71}  # Fix deployed

   Confidence: 0.87 ✓
   Key Shift: joy→anger at t=24h (trigger: login bug)
   Recovery: anger→trust at t=36h (trigger: rapid fix + communication)
   ```

2. **Regional Analysis:**
   ```python
   regions = {
       'North America': {'anger': 0.52, 'sample': 1247, 'conf': 0.89},
       'Europe': {'neutral': 0.48, 'sample': 892, 'conf': 0.82},
       'Asia-Pacific': {'joy': 0.61, 'sample': 634, 'conf': 0.78}
   }

   Insight: Bug affected NA primarly (timezone timing)
   Polarization: 0.64 (moderate - NA negative, APAC positive)
   ```

3. **Influence Network:**
   ```python
   influencers = [
       {'user': '@techreview', 'reach': 450K, 'sentiment': 'anger→trust'},
       {'user': '@saasexpert', 'reach': 280K, 'sentiment': 'neutral'},
       {'user': '@earlyadopter', 'reach': 95K, 'sentiment': 'joy'}
   ]

   Cascade: @techreview post reached 1.2M (amplification: 2.7x)
   Echo chambers: 2 detected (pro-product + frustrated-users)
   ```

**Output:**
- **Dominant sentiment:** Initial positive → temporary negative → strong recovery
- **Risk assessment:** Medium (polarization 0.64, but recovery trend positive)
- **Recommendations:**
  1. Continue transparent communication (trust rebuilding)
  2. Target NA region with personalized outreach
  3. Amplify @techreview's positive recovery message
  4. Monitor frustrated-users echo chamber for escalation

