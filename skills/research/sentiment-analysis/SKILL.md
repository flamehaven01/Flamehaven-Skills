---
name: sentiment-analysis
description: Multi-dimensional emotion and sentiment analysis - combines EmotionFlowLLM, political sentiment mapping, and influence network detection for comprehensive social signal intelligence
---

# Sentiment Analysis & Emotion Intelligence

## Overview

Surface sentiment is noise. Deep emotion without structure is guesswork.

**Core principle:** ALWAYS analyze multi-dimensional emotion flow with temporal tracking and influence network mapping.

## The Iron Law

```
NO SENTIMENT REPORT WITHOUT EMOTION FLOW VALIDATION
Confidence Score ≥ 0.75 REQUIRED
```

## When to Use

Use for ANY sentiment analysis task:
- Social media monitoring
- Customer feedback analysis
- Political sentiment tracking
- Brand reputation management
- Market research and trend detection
- Crisis communication monitoring

**Use this ESPECIALLY when:**
- Multiple emotion dimensions present
- Temporal patterns matter (emotion shifts over time)
- Influence networks affect sentiment spread
- Regional/demographic segmentation needed
- High-stakes decision based on sentiment

## Three-Layer Analysis

### Layer 1: EmotionFlowLLM (Multi-Dimensional Detection)

**BEFORE aggregation:**

1. **10-Dimension Emotion Vector**
   ```python
   emotion_vector = {
       'joy': 0.0 - 1.0,        # Happiness, satisfaction
       'sadness': 0.0 - 1.0,    # Disappointment, grief
       'anger': 0.0 - 1.0,      # Frustration, rage
       'fear': 0.0 - 1.0,       # Anxiety, concern
       'surprise': 0.0 - 1.0,   # Shock, unexpectedness
       'disgust': 0.0 - 1.0,    # Rejection, revulsion
       'trust': 0.0 - 1.0,      # Confidence, reliability
       'anticipation': 0.0 - 1.0, # Expectation, hope
       'neutral': 0.0 - 1.0,    # Factual, unemotional
       'mixed': 0.0 - 1.0       # Conflicting emotions
   }
   ```

2. **Emotion Flow Tracking**
   ```python
   # Track emotion changes over time
   emotion_flow = []
   for timestamp, content in temporal_data:
       emotion = detect_emotion(content)
       emotion_flow.append({
           'time': timestamp,
           'emotion': emotion,
           'intensity': calculate_intensity(content),
           'trigger': identify_trigger(content, prev_context)
       })

   # Detect shifts
   shifts = detect_emotion_shifts(emotion_flow)
   # Example: joy→anger (trigger: policy announcement)
   ```

3. **Confidence Scoring**
   ```python
   confidence = calculate_confidence(
       text_length=len(content),
       emotion_clarity=emotion_vector_entropy,
       context_availability=has_temporal_context,
       language_quality=grammar_score
   )

   if confidence < 0.75:
       FLAG_LOW_CONFIDENCE()
   ```

**Threshold:** Confidence ≥ 0.75 required

### Layer 2: Political Sentiment Mapping (Regional Analysis)

**WHEN regional/demographic context matters:**

1. **Geographic Sentiment Distribution**
   ```python
   sentiment_map = {}
   for region in regions:
       regional_data = filter_by_region(data, region)
       sentiment_map[region] = {
           'dominant_emotion': get_dominant_emotion(regional_data),
           'intensity': calculate_regional_intensity(regional_data),
           'velocity': calculate_sentiment_change_rate(regional_data),
           'sample_size': len(regional_data),
           'confidence': calculate_confidence(regional_data)
       }
   ```

2. **Demographic Segmentation**
   ```python
   segments = ['age_group', 'gender', 'education', 'income', 'political_leaning']

   for segment in segments:
       segment_analysis = analyze_by_segment(data, segment)
       if segment_analysis['variance'] > threshold:
           FLAG_SIGNIFICANT_DIFFERENCE(segment)
   ```

3. **Polarization Detection**
   ```python
   # Measure opinion distribution
   polarization_score = calculate_polarization(sentiment_distribution)

   # 0.0-0.3: Consensus
   # 0.3-0.7: Moderate disagreement
   # 0.7-1.0: High polarization

   if polarization_score >= 0.7:
       ALERT_HIGH_POLARIZATION()
   ```

**Threshold:** Sample size ≥ 100 per region, confidence ≥ 0.75

### Layer 3: Influence Network Detection (Propagation Analysis)

**WHEN understanding sentiment spread:**

1. **Identify Influencers**
   ```python
   influencers = []
   for user in users:
       influence_score = calculate_influence(
           followers=user.followers,
           engagement_rate=user.avg_engagement,
           reach=user.estimated_reach,
           credibility=user.credibility_score
       )

       if influence_score > threshold:
           influencers.append({
               'user': user,
               'influence': influence_score,
               'sentiment': detect_sentiment(user.content),
               'reach': estimate_reach(user)
           })
   ```

2. **Cascade Analysis**
   ```python
   # Track how sentiment spreads
   cascade = build_propagation_tree(
       seed_posts=initial_posts,
       time_window='48h',
       depth=3  # levels of sharing
   )

   cascade_metrics = {
       'virality': calculate_virality(cascade),
       'speed': calculate_propagation_speed(cascade),
       'amplification': calculate_amplification_factor(cascade),
       'mutation': detect_sentiment_mutation(cascade)
   }
   ```

3. **Echo Chamber Detection**
   ```python
   # Identify isolated clusters with reinforcing sentiment
   clusters = detect_communities(network_graph)

   for cluster in clusters:
       homogeneity = calculate_sentiment_homogeneity(cluster)
       isolation = calculate_cluster_isolation(cluster, network_graph)

       if homogeneity > 0.85 and isolation > 0.7:
           FLAG_ECHO_CHAMBER(cluster)
   ```

**Threshold:** Network coverage ≥ 70%, cascade depth ≥ 2 levels

## Integrated Flow

```
Input Data (text, social media, feedback)
    ↓
[EmotionFlowLLM]
    ├─ 10-dimension emotion detection
    ├─ Temporal emotion flow tracking
    └─ Confidence scoring
    ↓
[Regional/Demographic Mapping]
    ├─ Geographic sentiment distribution
    ├─ Demographic segmentation
    └─ Polarization detection
    ↓
[Influence Network Analysis]
    ├─ Influencer identification
    ├─ Cascade propagation tracking
    └─ Echo chamber detection
    ↓
[Synthesis & Insights]
    ├─ Dominant sentiment trends
    ├─ Key drivers and triggers
    ├─ Risk assessment
    └─ Actionable recommendations
    ↓
OUTPUT: Multi-dimensional sentiment report + confidence scores + recommendations
```

## Red Flags

- "Just tell me positive or negative"
- "We don't need temporal tracking"
- "Skip the demographic breakdown"
- "Influencer analysis is optional"
- "Low confidence is fine"

**ALL mean: STOP. Run full sentiment analysis.**

## Integration

**REQUIRED by:**
- `crisis-communication` - Real-time sentiment monitoring
- `brand-strategy` - Reputation management
- `political-analysis` - Public opinion tracking

**Complementary:**
- `fact-checking` - Validate sentiment triggers (claims)
- `sovereign-search` - Source verification for sentiment data
- `strategic-consulting` - Customer feedback integration

## Example: Product Launch Sentiment

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

## Verification Checklist

- [ ] 10-dimension emotion vector calculated
- [ ] Temporal emotion flow tracked
- [ ] Confidence score ≥ 0.75
- [ ] Regional sentiment mapped (if applicable)
- [ ] Demographic segmentation completed (if applicable)
- [ ] Polarization score calculated
- [ ] Influencers identified
- [ ] Cascade propagation analyzed
- [ ] Echo chambers detected
- [ ] Actionable insights generated
- [ ] TraceVault logged

## Final Rule

```
Sentiment Report → Confidence ≥ 0.75 AND Multi-dimensional AND Temporally tracked
Otherwise → insufficient for decisions
```

Surface sentiment misleads. Structure reveals truth.
