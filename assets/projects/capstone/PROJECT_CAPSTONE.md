> **Note:** This document is a summarized design process overview created for portfolio review. It is not the full 110+ page capstone report.

# The Stack: Wearable Hip Protector for Fall-Injury Prevention

**Course:** MCG 4366: Capstone Design Project (University of Ottawa)

**Team:** Ajeet Krishnasamy, Hussein Madi, Bao-Tran Do, Gabrielle Graceffa, Yasmin Elkalish, Chelse Rose Vadakkeveettilan Hilariyos

**Timeline:** September 2025 - April 2026

---

## Executive Summary

The Stack is a wearable hip protection system designed to reduce femoral fracture risk during lateral and posterolateral falls in older adults. The project delivers a complete design lifecycle: problem definition through literature review, concept generation and scoring, detailed mechanical analysis, a MATLAB-based patient parametrization tool, a SolidWorks-integrated CAD pipeline, FEA validation, and economic/ethical evaluation. The final design uses a horseshoe-shaped multilayer pad (STF core + TPU shell) integrated into a garment with Velcro adjustability, targeting >35% force attenuation at under 600 g device mass.

---

## 1. Problem & Motivation

### 1.1 Clinical Context
- Hip fractures are a leading cause of morbidity/mortality in adults aged 65+
- ~20% of patients do not survive the first year post-fracture
- Healthcare costs projected to exceed $25B annually in North America
- Lateral and posterolateral falls generate impact forces exceeding femoral fracture thresholds

### 1.2 Biomechanical Mechanism
- Greater trochanter (GT) is the primary impact site during sideways falls
- Impact velocities average 2.14-3.0 m/s for pelvis impact
- Effective mass acting on the hip: m_eff = 0.724 * weight - 4.67 (kg)
- Trochanteric soft tissue thickness (STT) varies by BMI and gender: natural attenuation is often insufficient

### 1.3 The Compliance Gap
- Commercial hip protectors show measurable force reduction in lab tests (2.5% to 40% attenuation)
- Real-world effectiveness is poor due to low user compliance
- Primary barriers: discomfort, bulkiness, poor fit, aesthetic concerns
- Pad displacement of just 3 cm increases peak femoral neck forces by 23%

---

## 2. Literature Review

### 2.1 Key Findings
- **Materials:** Shear-thickening fluids (STF) achieve higher peak force reduction than conventional foams due to rate-dependent stiffening. TPU provides structural support and flexibility.
- **Geometry:** Large horseshoe and donut-shaped pads outperform closed-oval shapes (35-40% vs 15-25% attenuation). Energy shunting (redirecting force around GT) is as important as energy absorption.
- **Anthropometry:** 5th-95th percentile design accommodates 80% of the population. Gender-specific differences in STT, hip breadth, and body segment ratios require separate regression equations.
- **Standards:** ISO 10993 (biocompatibility), EN 1621-1 (impact protection), Class I medical device framework.

### 2.2 Commercial & Research Landscape
- **Hard-shell:** Force shunting through rigid dome (e.g., SafetyPants)
- **Soft-shell:** Foam-based energy absorption (e.g., HipSaver)
- **Hybrid:** Combined hard/soft layers
- **Airbag:** Wearable airbag systems (active detection)
- **Research:** STF composites, auxetic structures, 3D-printed lattices
- **Gap identified:** No existing solution adequately balances protection AND comfort for consistent daily wear

---

## 3. Design Requirements

| Parameter | Target | Source |
|-----------|--------|--------|
| Force attenuation | >= 35% | Literature benchmark (top-quartile commercial) |
| Max pad thickness | 24 mm | Wearability constraint |
| Max device mass | 600 g | Comfort for daily wear |
| Sizing range | 5th-95th percentile (hip circ ~85-115 cm) | Population coverage |
| Pad positioning | Within +/-10 mm of GT | Biomechanical studies |
| Regulatory | Class I medical device | ISO 10993, EN 1621-1 |
| Retail price | $70-120 CAD | Market competitiveness |

---

## 4. Conceptual Design

### 4.1 System Architecture (3 Subsystems)
1. **Injury Prevention** : pad geometry, material selection, impact absorption
2. **Adjustability & Wearability** : garment fit, fastening, comfort
3. **Fall Detection** : sensor-based impact detection (scoped out after conceptual phase)

### 4.2 Concept Generation & Scoring
Each subsystem generated 3-5 concepts, scored on weighted criteria:
- **Injury Prevention:** STF composite (score: 4.2/5) > EVA foam (3.6) > airbag (3.4) > spacer fabric (3.2) > hard shell (3.0)
- **Garment Fit:** Open-crotch shorts with Velcro (4.0) > belt/patch (3.2) > full pants (2.6)
- **Fastening:** Velcro straps (4.2) > elastic band (3.8) > zipper (3.0)
- **Materials (scored separately):** STF/D3O (4.6) > TPU/NinjaFlex (4.2) > EVA (3.6)

### 4.3 Final Concept Selection
- **Padding:** Multilayer STF composite + TPU shell (horseshoe shape)
- **Garment:** Breathable shorts with open-crotch design
- **Fastening:** Velcro adjustable belts at waist and thighs
- **Textile:** Nylon-spandex for stretch, breathability, durability

---

## 5. Final Design: "The Stack"

### 5.1 Padding Sub-Assembly
- **Geometry:** Horseshoe-shaped pad positioned over greater trochanter
- **Cross-section:** TPU-STF-TPU sandwich (3 layers in series)
  - Outer TPU layers: structural shell, flexibility, skin contact safety
  - STF core: rate-dependent stiffening, energy absorption
- **Dimensions (sample, 70 kg female):**
  - Outer diameter: ~15.5 cm
  - Inner diameter: ~5.4 cm
  - Pad height: ~19.0 cm
  - Total thickness: 14-24 mm (patient-optimized)
  - Radius of curvature: ~34.4 cm (matches hip contour)
  - Fillet radius: 1.5 cm (comfort edge)
- **Pad surface area:** ~150-180 cm²
- **Pad mass (each):** ~65-80 g (varies with thickness)

### 5.2 Garment Sub-Assembly
- Nylon-spandex textile base shorts
- Open-crotch design for dignity and bathroom convenience
- Velcro waistband (adjustable, +15 cm overlap allowance)
- Velcro thigh straps (5 cm width, adjustable circumference)
- Fabric panel dimensions scale with height and BMI
- **Total garment mass:** ~350-440 g (combined with 2 pads: ~510 g total)

### 5.3 Key Design Decisions
1. **Horseshoe over donut:** Horseshoe redirects force into surrounding soft tissue (energy shunting) while donut primarily absorbs. Horseshoe also breathes better for comfort.
2. **STF over D3O:** STF literature is open-access; D3O is proprietary with restricted data. Selected STF as equivalent with publishable parameters.
3. **Open-crotch:** Directly addresses the #1 compliance complaint in literature: difficulty with bathroom use.
4. **Garment-integrated over patch:** Permanently sewn-in pads ensure consistent GT positioning; removable pads risk misalignment.

---

## 6. Working Analysis

### 6.1 Anthropometric Model
Gender-specific regression equations derived from NHANES/Hsiao anthropometric data: **STT (mm):**
- Female: STT = 2.3415 * BMI - 33.444
- Male: STT = 3.4795 * BMI - 38.015

**Soft tissue stiffness:**
- Female: k_st = 71,060 N/m, c_st = 1,000 Ns/m
- Male: k_st = 90,440 N/m, c_st = 1,200 Ns/m

**Hip breadth:**
- B_hip = sqrt(2 * (C_hip / pi)^2 - D_hip^2) : elliptical cross-section assumption

### 6.2 Impact Physics (Kelvin-Voigt Viscoelastic Model)
- **Effective mass:** m_eff = 0.724 * weight - 4.67 (kg)
- **Impact velocity:** v = sqrt(2 * g * H_COM), where H_COM = 0.575 * height
- **System modeled as:** spring-damper in series (soft tissue + pad)

**Case I: No Padding:**
- Single spring-damper (soft tissue only)
- Natural frequency: omega_n1 = sqrt(k_st / m_eff)
- Damping ratio: zeta1 = c_st / (2 * sqrt(k_st * m_eff))
- Transmitted force: F_femur1 = c_st * v_dot + k_st * x

**Case II: With Padding:**
- Pad modeled as TPU-STF-TPU springs in series: - k_TPU = (E_TPU * A_pad) / t_TPU (E=12 MPa)
  - k_STF = (E_STF * A_pad) / t_STF (E=3.6 MPa)
  - k_pad = (1/k_TPU + 1/k_STF + 1/k_TPU)^(-1)
- Combined system: k_eq = (k_st * k_pad) / (k_st + k_pad)
- Transmitted force: F_femur2 = c_eq * v_dot + k_eq * x

### 6.3 Sample Calculations (70 kg Female, 165 cm)
| Parameter | Unprotected | Protected |
|-----------|-------------|-----------|
| Peak force | ~3,200 N | ~1,800 N |
| Attenuation | ---  | ~44% |
| t_pad (initial) | ---  | 14 mm |
| t_pad (optimized) | ---  | 17 mm |

### 6.4 Risk Assessment
Five safety factors evaluated:
1. **Compressive stress** : padding remains below material yield
2. **Bottoming out** : padding thickness prevents full compression
3. **Pressure distribution** : contact pressure below tissue damage threshold
4. **Femoral fracture** : transmitted force below fracture threshold (~3,000 N)
5. **Strain energy** : energy absorption within material limits

### 6.5 FEA Simulation
- **Setup:** SolidWorks static simulation, 1120 N applied load, simplified femur/soft tissue geometry
- **Results:**
  - Without pad: stress concentrated at femoral neck (~15 MPa)
  - With pad: stress distributed across pad surface (~6 MPa)
  - Displacement reduced by ~40% with padding
- **Drop test simulation:** Validated impact energy absorption across 0.5-1.0 m drop heights
- **Limitation:** STF modeled as linear elastic (not strain-rate dependent), likely underestimating true performance

---

## 7. Parametrization (MATLAB Tool)

### 7.1 Purpose
Convert 5 simple patient inputs into a complete, patient-specific design specification with SolidWorks integration.

### 7.2 Inputs
- Gender (Male/Female)
- Height (cm)
- Weight (kg)
- Hip circumference (cm)
- Waist circumference (cm)

### 7.3 Outputs
- Pad geometry (6 parameters for SolidWorks equations)
- Garment dimensions (6 parameters)
- Force analysis (peak forces, attenuation %)
- Optimized thickness (via iterative loop)
- Total device mass

### 7.4 Optimization Loop
1. Start: t_pad = 14 mm (4 mm TPU + 6 mm STF + 4 mm TPU)
2. Calculate k_TPU, k_STF, k_pad, k_eq, c_eq
3. Compute F_femur2 and Att_pad
4. IF Att_pad < 35% AND t_pad < 24 mm: - Increase t_TPU by 0.5 mm
   - Increase t_STF by 0.5 mm
   - Recalculate all stiffness/damping/force values
   - Repeat
5. Terminate when Att_pad >= 35% or t_pad >= 24 mm

### 7.5 SolidWorks Integration
- Exports `protector.txt` with 6 equations: h_pad, D_out, D_in, t_pad, R_curv, r_fillet
- Part file (`pad_part.SLDPRT`) reads these equations to auto-regenerate geometry
- Two assemblies: with padding (`Padding_Final.SLDASM`) and without (`No_padding.SLDASM`)

### 7.6 GUI Features (MATLAB App Designer)
- Input fields with labels and unit displays
- Generate button triggers Design_code.m
- Log file output with full calculation trace
- Path configuration for SolidWorks export

---

## 8. Economics

### 8.1 Cost Breakdown (per unit, 2,000 units)
| Category | Cost (CAD) |
|----------|------------|
| Materials (STF, TPU, fabric, Velcro) | $8-12 |
| Manufacturing (molding, assembly) | $10-15 |
| Logistics (packaging, distribution) | $5-8 |
| Regulatory (amortized) | $2-5 |
| **Total burdened cost** | ~$25-40 |
| **Recommended retail** | $70-120 |

### 8.2 Healthcare Cost-Benefit
- Cost-benefit ratio exceeds 25:1 when accounting for prevented hip fractures
- Average hip fracture hospitalization: ~$40,000 CAD
- Device cost: ~$100 CAD
- Number needed to treat to prevent one fracture is favorable at projected compliance rates

### 8.3 Sensitivity
- Optimal production scale: 2,000-5,000 units balances fixed cost absorption vs inventory risk
- Break-even at ~1,200 units at $90 retail price

---

## 9. Ethics & Regulatory

- **Patient safety:** ISO 10993 biocompatibility, EN 1621-1 impact protection
- **Informed consent:** Clear communication of protection limits (not fall-proof, risk reduction device)
- **Professional integrity:** Attenuation claims must be validated through standardized bench testing
- **Accessibility:** Inclusive sizing, climate adaptability, affordable pricing
- **Sustainability:** TPU and STF are not biodegradable; end-of-life recycling plan needed
- **Conflict of interest:** No external funding influenced design decisions

---

## 10. Results & Discussion

### 10.1 What Worked
- Analytical model consistently showed force attenuation improvement with padding
- FEA confirmed stress reduction at femoral neck with pad in place
- Parametrization tool successfully generates patient-specific geometries from limited inputs
- SolidWorks integration automates CAD regeneration

### 10.2 Limitations
- **Material model:** STF approximated as linear elastic (E=3.6 MPa constant). True STF stiffens by 2-3x at high strain rates, meaning real-world performance likely exceeds predictions
- **Force discrepancy:** Numerical residual between hand calculations and MATLAB output (unit conversion, damping approximation, or time-step resolution)
- **Prototype scope:** Full garment prototype was not fabricated; analysis focused on padding stack
- **No experimental validation:** Impact testing with instrumented drop tower was out of scope due to budget/timeline
- **Commercial benchmarking:** Certified hip protectors cost prohibitive for comparison testing

### 10.3 Future Work
1. Acquire D3O or equivalent proprietary STF for realistic material characterization
2. Build full-garment prototype with integrated padding
3. Design and build instrumented drop tower test rig
4. ISO-aligned standardized impact testing
5. Comparative benchmarking against commercial protectors
6. Clinical trial for comfort, compliance, and real-world efficacy

---

## 11. Team Contributions

| Member | Primary Role |
|--------|-------------|
| Ajeet Krishnasamy | Project management, conceptual design, MATLAB GUI development |
| Hussein Madi | Literature review, force analysis, economics |
| Bao-Tran Do | Parametrization lead, working analysis, SolidWorks integration |
| Gabrielle Graceffa | Working analysis, FEA simulation |
| Yasmin Elkalish | Market analysis, manufacturing cost model |
| Chelse Rose Vadakkeveettilan Hilariyos | Ethics, regulatory compliance, standards research |

---

## 12. Tools & Technologies

- **CAD:** SolidWorks (parts, assemblies, FEA simulation)
- **Analysis:** MATLAB (App Designer GUI, numerical optimization), hand calculations (Kelvin-Voigt)
- **FEA:** SolidWorks Simulation (static, drop test)
- **Standards:** ISO 10993, EN 1621-1, CSA Z62x, ASTM F355
- **Documentation:** Microsoft Word, LaTeX-style equations

---