/**
 * SIH26044 Skill, Internship and Placement Portal
 * Frontend Application Controller & Bilingual i18n Engine
 */

// ==========================================
// 1. BILINGUAL DICTIONARY (EN / HI)
// ==========================================
const TRANSLATIONS = {
  en: {
    portalTitle: "SIH26044 — Skill, Internship & Placement Portal",
    portalSubtitle: "AI-Powered Resume Parsing, Skill Gap Vectorization & Smart Recommendations",
    tabStudent: "Student Hub",
    tabRecruiter: "Recruiter Portal",
    tabTpo: "TPO Analytics",
    tabArch: "Architecture & Logic",
    
    // Student Hub
    resumeUploadHeader: "Upload Resume (PDF)",
    resumeUploadSub: "AI parses explicit competencies and infers implicit project skills",
    dragDropText: "Drag & drop your resume PDF here or click to browse",
    orTrySample: "Or test immediately with pre-loaded profiles:",
    sampleWeb: "Full Stack Developer",
    sampleAI: "AI & Data Science",
    sampleCore: "Core CS & Systems",
    
    extractedProfileTitle: "Extracted Candidate Profile",
    departmentLabel: "Department:",
    cgpaLabel: "CGPA / Grade:",
    educationLabel: "Education:",
    verifiedSkillsTitle: "Verified Skills & Confidence",
    addSkillPlaceholder: "Add a skill (e.g., Docker, Kotlin)...",
    btnAddSkill: "Add",
    
    // Skill Gap & Radar
    gapAnalysisTitle: "Skill Gap Analysis & Target Role Benchmark",
    selectTargetRole: "Select Target Internship / Role:",
    matchScoreLabel: "Match Score",
    readinessTitle: "Placement Readiness Rating:",
    matchedSkillsTitle: "Matched Competencies",
    missingSkillsTitle: "Missing / High Priority Skills to Acquire",
    radarTitle: "Radar Competency Vectors (Candidate vs Role Requirement)",
    explainabilityTitle: "Explainable AI Match Rationale",
    
    // Recommendations
    recommendationsTitle: "Ranked Internship & Job Opportunities",
    filterSector: "All Sectors",
    filterRemote: "Remote Only",
    applyBtn: "Apply Now",
    appliedSuccess: "Application submitted successfully! Recruiter notified.",
    
    // Upskilling
    upskillingTitle: "Personalized Upskilling Roadmap (SWAYAM / NPTEL / MOOCs)",
    upskillingSub: "Curated free government and open courses to close your identified skill gaps",
    markCompleted: "Mark Complete",
    
    // Recruiter Portal
    postJobTitle: "Post New Internship / Job Opening",
    jobTitleLabel: "Job Title",
    companyLabel: "Company Name",
    sectorLabel: "Industry Sector",
    locationLabel: "Location",
    stipendLabel: "Stipend / Salary",
    reqSkillsLabel: "Required Skills (comma separated)",
    prefSkillsLabel: "Preferred Skills (comma separated)",
    btnPostJob: "Publish Opportunity",
    rankedCandidatesTitle: "Ranked Candidate Shortlist for Position:",
    candidateName: "Candidate",
    candidateDept: "Department & CGPA",
    candidateScore: "Match Score",
    candidateSkills: "Skill Overlap",
    candidateStatus: "Action / Status",
    
    // TPO Dashboard
    tpoTitle: "Institution Placement Readiness & Batch Analytics",
    totalStudents: "Total Tracked Students",
    placementReadyPct: "Placement Ready Rate",
    avgReadiness: "Batch Avg Readiness Score",
    heatmapTitle: "Department-wise Skill Gap Heatmap (%)",
    missingSkillsChartTitle: "Most Common Missing Skills Across Batch",
    btnExportCsv: "Export Placement Readiness Report (CSV)",
    
    // Status badges
    bestFit: "Best Fit",
    stretch: "Stretch Opportunity",
    safe: "Safe Match"
  },
  hi: {
    portalTitle: "SIH26044 — कौशल, इंटर्नशिप एवं प्लेसमेंट पोर्टल",
    portalSubtitle: "एआई आधारित रिज्यूम पार्सिंग, स्किल गैप मैपिंग एवं स्मार्ट सिफारिशें",
    tabStudent: "विद्यार्थी हब (Student Hub)",
    tabRecruiter: "भर्तीकर्ता पोर्टल (Recruiter)",
    tabTpo: "टीपीओ विश्लेषण (TPO Analytics)",
    tabArch: "सिस्टम आर्किटेक्चर",
    
    // Student Hub
    resumeUploadHeader: "अपना बायोडाटा (PDF) अपलोड करें",
    resumeUploadSub: "एआई आपके प्रोजेक्ट्स और अनुभवों से छिपे हुए कौशल भी निकालता है",
    dragDropText: "पीडीएफ फ़ाइल यहाँ खींचें या ब्राउज़ करने के लिए क्लिक करें",
    orTrySample: "या तुरंत टेस्ट करने के लिए सैंपल प्रोफाइल चुनें:",
    sampleWeb: "फुल स्टैक डेवलपर",
    sampleAI: "एआई और डेटा साइंस",
    sampleCore: "कोर सीएस और सिस्टम्स",
    
    extractedProfileTitle: "निकाला गया उम्मीदवार प्रोफाइल",
    departmentLabel: "विभाग (Department):",
    cgpaLabel: "सीजीपीए (CGPA):",
    educationLabel: "शिक्षा (Education):",
    verifiedSkillsTitle: "सत्यापित कौशल और विश्वसनीयता स्कोर",
    addSkillPlaceholder: "कौशल जोड़ें (उदा. Docker, Kotlin)...",
    btnAddSkill: "जोड़ें",
    
    // Skill Gap & Radar
    gapAnalysisTitle: "स्किल गैप विश्लेषण एवं लक्षित भूमिका तुलना",
    selectTargetRole: "लक्षित इंटर्नशिप / जॉब रोल चुनें:",
    matchScoreLabel: "मैच स्कोर (Match Score)",
    readinessTitle: "प्लेसमेंट तत्परता रेटिंग:",
    matchedSkillsTitle: "मेल खाने वाले कौशल (Matched Skills)",
    missingSkillsTitle: "कमी वाले कौशल जो सीखने आवश्यक हैं (Missing Skills)",
    radarTitle: "रडार सक्षमता वेक्टर (उम्मीदवार बनाम जॉब की आवश्यकता)",
    explainabilityTitle: "एआई स्कोर व्याख्या (Explainable AI)",
    
    // Recommendations
    recommendationsTitle: "रैंक की गई उपयुक्त इंटर्नशिप व नौकरियां",
    filterSector: "सभी क्षेत्र",
    filterRemote: "केवल रिमोट (Remote Only)",
    applyBtn: "आवेदन करें",
    appliedSuccess: "सफलतापूर्वक आवेदन किया गया! रिक्रूटर को सूचित कर दिया गया है।",
    
    // Upskilling
    upskillingTitle: "व्यक्तिगत कौशल उन्नयन मार्ग (SWAYAM / NPTEL / कोर्सेरा)",
    upskillingSub: "कमी वाले कौशलों को पूरा करने के लिए भारत सरकार के स्वयं एवं एनपीटीईएल पाठ्यक्रम",
    markCompleted: "पूर्ण चिह्नित करें",
    
    // Recruiter Portal
    postJobTitle: "नई इंटर्नशिप / जॉब पोस्ट करें",
    jobTitleLabel: "पद का नाम (Job Title)",
    companyLabel: "कंपनी का नाम",
    sectorLabel: "उद्योग क्षेत्र (Sector)",
    locationLabel: "स्थान (Location)",
    stipendLabel: "वजीफा / वेतन (Stipend)",
    reqSkillsLabel: "अनिवार्य कौशल (अल्पविराम से अलग करें)",
    prefSkillsLabel: "प्राथमिकता वाले कौशल",
    btnPostJob: "अवसर प्रकाशित करें",
    rankedCandidatesTitle: "पद हेतु रैंक किए गए शीर्ष उम्मीदवार:",
    candidateName: "उम्मीदवार",
    candidateDept: "विभाग व सीजीपीए",
    candidateScore: "मैच स्कोर",
    candidateSkills: "कौशल ओवरलैप",
    candidateStatus: "कार्रवाई / स्थिति",
    
    // TPO Dashboard
    tpoTitle: "संस्थान प्लेसमेंट तत्परता एवं बैच विश्लेषण",
    totalStudents: "कुल नामांकित छात्र",
    placementReadyPct: "प्लेसमेंट हेतु तैयार दर (%)",
    avgReadiness: "बैच औसत तत्परता स्कोर",
    heatmapTitle: "विभाग अनुसार स्किल गैप हीटमैप (%)",
    missingSkillsChartTitle: "बैच में सबसे अधिक कमी वाले प्रमुख कौशल",
    btnExportCsv: "प्लेसमेंट रिपोर्ट डाउनलोड करें (CSV)",
    
    // Status badges
    bestFit: "उत्कृष्ट मैच (Best Fit)",
    stretch: "प्रयास अवसर (Stretch)",
    safe: "सुरक्षित मैच (Safe)"
  }
};

// Application State
const state = {
  lang: 'en',
  currentTab: 'student',
  jobs: [],
  selectedJobId: null,
  profile: null,
  gapAnalysis: null,
  recommendations: [],
  upskillingCourses: [],
  tpoAnalytics: null,
  radarChartInstance: null,
  tpoChartInstance: null
};

// ==========================================
// 2. INITIALIZATION & LIFECYCLE
// ==========================================
document.addEventListener('DOMContentLoaded', async () => {
  setupNavigation();
  setupUploadHandlers();
  await loadJobs();
  await loadSampleResume('sample_web_dev'); // Default start with full stack student
  await loadTPOAnalytics();
  applyLanguage(state.lang);
});

function setupNavigation() {
  const tabs = ['student', 'recruiter', 'tpo', 'arch'];
  tabs.forEach(tab => {
    const btn = document.getElementById(`nav-${tab}`);
    if (btn) {
      btn.addEventListener('click', () => switchTab(tab));
    }
  });

  // Language switchers
  const btnEn = document.getElementById('lang-en');
  const btnHi = document.getElementById('lang-hi');
  if (btnEn && btnHi) {
    btnEn.addEventListener('click', () => setLanguage('en'));
    btnHi.addEventListener('click', () => setLanguage('hi'));
  }

  // Filter handlers
  document.getElementById('filter-sector')?.addEventListener('change', refreshRecommendations);
  document.getElementById('filter-remote')?.addEventListener('change', refreshRecommendations);
  document.getElementById('job-selector')?.addEventListener('change', (e) => {
    state.selectedJobId = e.target.value;
    triggerGapAnalysis();
  });
}

function switchTab(tabName) {
  state.currentTab = tabName;
  ['student', 'recruiter', 'tpo', 'arch'].forEach(t => {
    const section = document.getElementById(`section-${t}`);
    const navBtn = document.getElementById(`nav-${t}`);
    if (section) section.classList.toggle('hidden', t !== tabName);
    if (navBtn) {
      if (t === tabName) {
        navBtn.classList.add('bg-indigo-600', 'text-white', 'shadow-sm');
        navBtn.classList.remove('text-slate-600', 'hover:bg-slate-100');
      } else {
        navBtn.classList.remove('bg-indigo-600', 'text-white', 'shadow-sm');
        navBtn.classList.add('text-slate-600', 'hover:bg-slate-100');
      }
    }
  });

  if (tabName === 'recruiter') {
    loadRecruiterCandidates(state.selectedJobId || (state.jobs[0] ? state.jobs[0].id : 'job-101'));
  } else if (tabName === 'tpo') {
    renderTPOVisuals();
  }
}

function setLanguage(lang) {
  state.lang = lang;
  document.getElementById('lang-en')?.classList.toggle('font-bold', lang === 'en');
  document.getElementById('lang-en')?.classList.toggle('text-indigo-600', lang === 'en');
  document.getElementById('lang-hi')?.classList.toggle('font-bold', lang === 'hi');
  document.getElementById('lang-hi')?.classList.toggle('text-indigo-600', lang === 'hi');
  applyLanguage(lang);
  if (state.gapAnalysis) renderRadarChart();
}

function applyLanguage(lang) {
  const dict = TRANSLATIONS[lang] || TRANSLATIONS.en;
  document.querySelectorAll('[data-i18n]').forEach(elem => {
    const key = elem.getAttribute('data-i18n');
    if (dict[key]) {
      elem.textContent = dict[key];
    }
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(elem => {
    const key = elem.getAttribute('data-i18n-placeholder');
    if (dict[key]) {
      elem.placeholder = dict[key];
    }
  });
}

// ==========================================
// 3. API CALLS & DATA SYNC
// ==========================================

async function loadJobs() {
  try {
    const res = await fetch('/api/recruiter/jobs');
    const data = await res.json();
    state.jobs = data;
    
    // Populate job selectors
    const selector = document.getElementById('job-selector');
    const recruiterJobSelector = document.getElementById('recruiter-job-selector');
    if (selector) {
      selector.innerHTML = state.jobs.map(j => `<option value="${j.id}">${j.title} (${j.company})</option>`).join('');
      state.selectedJobId = state.jobs[0]?.id;
    }
    if (recruiterJobSelector) {
      recruiterJobSelector.innerHTML = state.jobs.map(j => `<option value="${j.id}">${j.title} (${j.company})</option>`).join('');
      recruiterJobSelector.addEventListener('change', (e) => loadRecruiterCandidates(e.target.value));
    }
  } catch (err) {
    console.error("Failed to load jobs:", err);
  }
}

async function loadSampleResume(sampleKey) {
  showLoader(true);
  try {
    const res = await fetch(`/api/resume/sample/${sampleKey}`);
    const data = await res.json();
    state.profile = data;
    renderProfile();
    await triggerGapAnalysis();
    await refreshRecommendations();
  } catch (err) {
    console.error("Failed to load sample:", err);
  } finally {
    showLoader(false);
  }
}

async function uploadPdfFile(file) {
  showLoader(true);
  try {
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('/api/resume/upload', {
      method: 'POST',
      body: formData
    });
    if (!res.ok) throw new Error("Parsing failed");
    const data = await res.json();
    state.profile = data;
    renderProfile();
    await triggerGapAnalysis();
    await refreshRecommendations();
  } catch (err) {
    alert("Error parsing resume: " + err.message);
  } finally {
    showLoader(false);
  }
}

async function triggerGapAnalysis() {
  if (!state.profile || !state.selectedJobId) return;
  const studentSkillNames = state.profile.skills.map(s => s.name);
  try {
    const res = await fetch('/api/gap-analysis', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_skills: studentSkillNames,
        job_id: state.selectedJobId
      })
    });
    state.gapAnalysis = await res.json();
    renderGapAnalysis();
    renderRadarChart();
    
    // Fetch upskilling for missing skills
    const missingSkillNames = state.gapAnalysis.missing_skills.map(m => m.name);
    if (missingSkillNames.length > 0) {
      const upRes = await fetch('/api/upskilling', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ missing_skills: missingSkillNames })
      });
      state.upskillingCourses = await upRes.json();
      renderUpskillingCards();
    } else {
      state.upskillingCourses = [];
      renderUpskillingCards();
    }
  } catch (err) {
    console.error("Error running gap analysis:", err);
  }
}

async function refreshRecommendations() {
  if (!state.profile) return;
  const sector = document.getElementById('filter-sector')?.value || 'All';
  const remoteOnly = document.getElementById('filter-remote')?.checked || false;
  
  try {
    const res = await fetch('/api/recommendations', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        student_skills: state.profile.skills.map(s => s.name),
        sector: sector,
        remote_only: remoteOnly
      })
    });
    state.recommendations = await res.json();
    renderRecommendations();
  } catch (err) {
    console.error("Error fetching recommendations:", err);
  }
}

async function loadRecruiterCandidates(jobId) {
  try {
    const res = await fetch(`/api/recruiter/candidates/${jobId}`);
    const candidates = await res.json();
    renderCandidates(candidates, jobId);
  } catch (err) {
    console.error("Failed to load candidates:", err);
  }
}

async function loadTPOAnalytics() {
  try {
    const res = await fetch('/api/tpo/analytics');
    state.tpoAnalytics = await res.json();
  } catch (err) {
    console.error("Failed to load TPO analytics:", err);
  }
}

// ==========================================
// 4. RENDERING & UI UPDATES
// ==========================================

function renderProfile() {
  const p = state.profile;
  if (!p) return;

  document.getElementById('profile-name').textContent = p.name;
  document.getElementById('profile-email').textContent = p.email;
  document.getElementById('profile-phone').textContent = p.phone;
  document.getElementById('profile-dept').textContent = p.department;
  document.getElementById('profile-summary').textContent = p.summary;
  
  // Render Education list
  const eduContainer = document.getElementById('profile-education');
  if (eduContainer) {
    eduContainer.innerHTML = p.education.map(e => `<li class="text-xs text-slate-600">${e}</li>`).join('');
  }

  // Render Skills tags with confidence
  renderSkillsTags();
}

function renderSkillsTags() {
  const container = document.getElementById('skills-badge-container');
  if (!container || !state.profile) return;

  container.innerHTML = state.profile.skills.map((s, idx) => {
    const confPct = Math.round(s.confidence * 100);
    const implicitBadge = s.is_implicit 
      ? `<span class="ml-1 text-[10px] bg-purple-100 text-purple-700 px-1 py-0.5 rounded font-mono">Implicit</span>` 
      : ``;
    return `
      <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-slate-100 text-slate-800 border border-slate-200 group hover:border-indigo-300 transition">
        <span>${s.name}</span>
        <span class="text-[10px] text-slate-400 font-mono">${confPct}%</span>
        ${implicitBadge}
        <button onclick="removeSkill(${idx})" class="text-slate-400 hover:text-red-500 ml-0.5 text-xs font-bold leading-none">&times;</button>
      </span>
    `;
  }).join('');
}

window.removeSkill = function(index) {
  if (!state.profile) return;
  state.profile.skills.splice(index, 1);
  renderSkillsTags();
  triggerGapAnalysis();
  refreshRecommendations();
};

window.addCustomSkill = function() {
  const input = document.getElementById('new-skill-input');
  const val = input.value.trim();
  if (!val || !state.profile) return;
  
  state.profile.skills.push({
    name: val,
    category: "User Added",
    confidence: 1.0,
    is_implicit: false,
    source: "Manual Addition"
  });
  input.value = '';
  renderSkillsTags();
  triggerGapAnalysis();
  refreshRecommendations();
};

function renderGapAnalysis() {
  const gap = state.gapAnalysis;
  if (!gap) return;

  // Score display
  const scoreElem = document.getElementById('match-score-display');
  const scoreDial = document.getElementById('match-score-circle');
  if (scoreElem) scoreElem.textContent = `${gap.match_score}%`;
  
  // Color styling based on score
  if (scoreDial) {
    if (gap.match_score >= 80) {
      scoreDial.className = "w-28 h-28 rounded-full border-4 border-emerald-500 bg-emerald-50 flex flex-col items-center justify-center shadow-inner";
    } else if (gap.match_score >= 55) {
      scoreDial.className = "w-28 h-28 rounded-full border-4 border-indigo-500 bg-indigo-50 flex flex-col items-center justify-center shadow-inner";
    } else {
      scoreDial.className = "w-28 h-28 rounded-full border-4 border-amber-500 bg-amber-50 flex flex-col items-center justify-center shadow-inner";
    }
  }

  // Category badge
  const catBadge = document.getElementById('match-category-badge');
  if (catBadge) {
    catBadge.textContent = gap.category;
    if (gap.category === "Best Fit") catBadge.className = "px-3 py-1 text-xs font-semibold rounded-full badge-best-fit";
    else if (gap.category === "Stretch Opportunities" || gap.category === "Stretch Opportunity") catBadge.className = "px-3 py-1 text-xs font-semibold rounded-full badge-stretch";
    else catBadge.className = "px-3 py-1 text-xs font-semibold rounded-full badge-safe";
  }

  // Readiness rating
  const readinessElem = document.getElementById('readiness-rating-text');
  if (readinessElem) readinessElem.textContent = gap.readiness_rating;

  // Matched skills pills
  const matchedContainer = document.getElementById('matched-skills-container');
  if (matchedContainer) {
    if (gap.matched_skills.length === 0) {
      matchedContainer.innerHTML = `<span class="text-xs text-slate-400">None matched directly</span>`;
    } else {
      matchedContainer.innerHTML = gap.matched_skills.map(s => `
        <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-emerald-100 text-emerald-800">
          <svg class="w-3 h-3 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
          ${s}
        </span>
      `).join('');
    }
  }

  // Missing skills pills
  const missingContainer = document.getElementById('missing-skills-container');
  if (missingContainer) {
    if (gap.missing_skills.length === 0) {
      missingContainer.innerHTML = `<span class="text-xs text-emerald-600 font-medium">All required skills present!</span>`;
    } else {
      missingContainer.innerHTML = gap.missing_skills.map(m => `
        <span class="inline-flex items-center px-2 py-0.5 rounded text-xs font-medium ${m.importance === 'High' ? 'bg-rose-100 text-rose-800 border border-rose-200' : 'bg-amber-100 text-amber-800'}">
          <span class="font-bold mr-1">${m.importance === 'High' ? '!' : 'o'}</span>
          ${m.name} (${m.domain})
        </span>
      `).join('');
    }
  }

  // Explainability text
  const expElem = document.getElementById('explainability-content');
  if (expElem) expElem.textContent = gap.explainability;
}

function renderRadarChart() {
  const gap = state.gapAnalysis;
  if (!gap) return;
  const canvas = document.getElementById('radarChartCanvas');
  if (!canvas) return;

  if (state.radarChartInstance) {
    state.radarChartInstance.destroy();
  }

  const isHindi = state.lang === 'hi';
  const labels = isHindi 
    ? ["प्रोग्रामिंग", "फ्रंटएंड", "बैकएंड व एपीआई", "डेटाबेस", "क्लाउड व देवऑप्स", "एआई व डेटा"]
    : gap.radar_labels;

  const ctx = canvas.getContext('2d');
  state.radarChartInstance = new Chart(ctx, {
    type: 'radar',
    data: {
      labels: labels,
      datasets: [
        {
          label: isHindi ? 'उम्मीदवार कौशल' : 'Candidate Competency',
          data: gap.student_vector,
          backgroundColor: 'rgba(79, 70, 229, 0.25)',
          borderColor: '#4f46e5',
          borderWidth: 2,
          pointBackgroundColor: '#4f46e5',
          pointRadius: 3
        },
        {
          label: isHindi ? 'भूमिका आवश्यकता' : 'Role Requirement',
          data: gap.role_vector,
          backgroundColor: 'rgba(239, 68, 68, 0.1)',
          borderColor: '#ef4444',
          borderWidth: 1.5,
          borderDash: [4, 4],
          pointBackgroundColor: '#ef4444',
          pointRadius: 2
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      scales: {
        r: {
          min: 0,
          max: 100,
          ticks: { display: false, stepSize: 20 },
          pointLabels: {
            font: { size: 11, family: 'Inter', weight: '600' },
            color: '#475569'
          },
          grid: { color: 'rgba(226, 232, 240, 0.8)' }
        }
      },
      plugins: {
        legend: {
          position: 'bottom',
          labels: { boxWidth: 12, font: { size: 11, family: 'Inter' } }
        }
      }
    }
  });
}

function renderRecommendations() {
  const container = document.getElementById('recommendations-container');
  if (!container) return;

  if (state.recommendations.length === 0) {
    container.innerHTML = `<div class="p-6 text-center text-slate-500">No matching jobs found for selected filters.</div>`;
    return;
  }

  container.innerHTML = state.recommendations.map(item => {
    const job = item.job;
    const badgeClass = item.category === "Best Fit" 
      ? "badge-best-fit" 
      : (item.category.includes("Stretch") ? "badge-stretch" : "badge-safe");
    
    return `
      <div class="glass-card rounded-xl p-5 border border-slate-200 hover:border-indigo-400 transition flex flex-col justify-between">
        <div>
          <div class="flex items-start justify-between gap-2 mb-2">
            <div>
              <span class="inline-block px-2.5 py-0.5 rounded-full text-xs font-semibold ${badgeClass} mb-1.5">
                ${item.category} (${item.match_score}%)
              </span>
              <h4 class="font-bold text-slate-900 text-base leading-snug">${job.title}</h4>
              <p class="text-xs text-slate-500 font-medium">${job.company} &bull; ${job.location} ${job.is_remote ? '<span class="text-indigo-600 font-semibold">(Remote)</span>' : ''}</p>
            </div>
            <div class="text-right">
              <span class="text-sm font-bold text-slate-800 block">${job.stipend_salary}</span>
              <span class="text-[11px] text-slate-400">${job.duration}</span>
            </div>
          </div>
          
          <p class="text-xs text-slate-600 mb-3 line-clamp-2">${job.description}</p>
          
          <div class="mb-3">
            <span class="text-[11px] font-semibold text-slate-500 block mb-1">Matched Skills:</span>
            <div class="flex flex-wrap gap-1">
              ${item.matched_skills.map(s => `<span class="px-2 py-0.5 bg-emerald-50 text-emerald-700 text-[11px] rounded font-medium">${s}</span>`).join('')}
            </div>
          </div>
          
          ${item.missing_skills.length > 0 ? `
            <div class="mb-3">
              <span class="text-[11px] font-semibold text-slate-500 block mb-1">To Learn:</span>
              <div class="flex flex-wrap gap-1">
                ${item.missing_skills.slice(0, 3).map(s => `<span class="px-2 py-0.5 bg-rose-50 text-rose-600 text-[11px] rounded font-medium">${s}</span>`).join('')}
              </div>
            </div>
          ` : ''}
        </div>
        
        <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
          <button onclick="selectJobForGap('${job.id}')" class="text-xs font-semibold text-indigo-600 hover:text-indigo-800">
            Compare Skill Gap &rarr;
          </button>
          <button onclick="applyToJob('${job.id}', this)" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-700 text-white text-xs font-semibold rounded-lg shadow-sm transition">
            Apply Now
          </button>
        </div>
      </div>
    `;
  }).join('');
}

window.selectJobForGap = function(jobId) {
  state.selectedJobId = jobId;
  const sel = document.getElementById('job-selector');
  if (sel) sel.value = jobId;
  triggerGapAnalysis();
  window.scrollTo({ top: document.getElementById('gap-analysis-card').offsetTop - 80, behavior: 'smooth' });
};

window.applyToJob = function(jobId, btn) {
  btn.textContent = "Applied \u2713";
  btn.classList.remove('bg-indigo-600', 'hover:bg-indigo-700');
  btn.classList.add('bg-emerald-600', 'text-white');
  btn.disabled = true;
  
  // Show toast notification
  showToast(TRANSLATIONS[state.lang].appliedSuccess);
};

function renderUpskillingCards() {
  const container = document.getElementById('upskilling-container');
  if (!container) return;

  if (state.upskillingCourses.length === 0) {
    container.innerHTML = `
      <div class="col-span-full p-8 text-center bg-white rounded-xl border border-slate-200">
        <svg class="w-10 h-10 text-emerald-500 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
        <p class="text-sm font-semibold text-slate-800">No skill gaps identified for the selected target role!</p>
        <p class="text-xs text-slate-500 mt-1">You already meet 100% of prerequisites.</p>
      </div>
    `;
    return;
  }

  container.innerHTML = state.upskillingCourses.map(course => {
    return `
      <div class="glass-card rounded-xl p-4 border border-slate-200 flex flex-col justify-between hover:shadow-md transition">
        <div>
          <div class="flex items-center justify-between mb-2">
            <span class="px-2 py-0.5 rounded text-[11px] font-bold bg-indigo-50 text-indigo-700 uppercase tracking-wide">
              ${course.skill}
            </span>
            <span class="text-[11px] font-semibold text-emerald-600 bg-emerald-50 px-2 py-0.5 rounded">
              ${course.is_free ? 'Free / Govt' : 'Paid'}
            </span>
          </div>
          <h5 class="font-bold text-sm text-slate-900 mb-1 leading-snug">${course.course_title}</h5>
          <p class="text-xs text-slate-500 font-medium mb-3">${course.provider} &bull; ${course.duration} &bull; ${course.level}</p>
        </div>
        <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
          <a href="${course.url}" target="_blank" rel="noopener noreferrer" class="text-xs font-semibold text-indigo-600 hover:underline flex items-center gap-1">
            <span>Explore Course</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
          </a>
          <label class="flex items-center text-xs text-slate-600 cursor-pointer">
            <input type="checkbox" onchange="toggleCourseProgress(this, '${course.skill}')" class="rounded border-slate-300 text-indigo-600 mr-1.5 focus:ring-indigo-500">
            <span class="text-[11px]">Enrolled</span>
          </label>
        </div>
      </div>
    `;
  }).join('');
}

window.toggleCourseProgress = function(checkbox, skillName) {
  if (checkbox.checked) {
    showToast(`Marked '${skillName}' upskilling as in-progress!`);
  }
};

// ==========================================
// 5. RECRUITER & TPO RENDERING
// ==========================================

function renderCandidates(candidates, jobId) {
  const container = document.getElementById('recruiter-candidates-tbody');
  if (!container) return;

  if (candidates.length === 0) {
    container.innerHTML = `<tr><td colspan="5" class="text-center py-6 text-slate-400">No candidates available.</td></tr>`;
    return;
  }

  container.innerHTML = candidates.map(c => {
    const scoreColor = c.match_score >= 80 ? 'text-emerald-600 bg-emerald-50' : (c.match_score >= 60 ? 'text-indigo-600 bg-indigo-50' : 'text-amber-600 bg-amber-50');
    return `
      <tr class="border-b border-slate-100 hover:bg-slate-50 transition">
        <td class="py-3 px-4 font-semibold text-slate-800 text-sm">${c.name}</td>
        <td class="py-3 px-4 text-xs text-slate-600">${c.department} &bull; CGPA ${c.cgpa}</td>
        <td class="py-3 px-4">
          <span class="px-2.5 py-1 rounded-full text-xs font-bold ${scoreColor}">
            ${c.match_score}%
          </span>
        </td>
        <td class="py-3 px-4">
          <div class="flex flex-wrap gap-1 max-w-xs">
            ${c.matched_skills.map(s => `<span class="px-1.5 py-0.5 bg-slate-100 text-slate-700 text-[10px] rounded">${s}</span>`).join('')}
          </div>
        </td>
        <td class="py-3 px-4">
          <select onchange="updateCandidateStatus('${jobId}', '${c.student_id}', this.value)" class="text-xs border border-slate-200 rounded-md p-1 bg-white focus:ring-indigo-500">
            <option value="Under Review" ${c.status === 'Under Review' ? 'selected' : ''}>Under Review</option>
            <option value="Shortlisted" ${c.status === 'Shortlisted' ? 'selected' : ''}>Shortlisted</option>
            <option value="Interview Scheduled" ${c.status === 'Interview Scheduled' ? 'selected' : ''}>Interview Scheduled</option>
            <option value="Offer Extended" ${c.status === 'Offer Extended' ? 'selected' : ''}>Offer Extended</option>
          </select>
        </td>
      </tr>
    `;
  }).join('');
}

window.updateCandidateStatus = async function(jobId, studentId, newStatus) {
  try {
    await fetch('/api/recruiter/status', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        job_id: jobId,
        student_id: studentId,
        status: newStatus
      })
    });
    showToast(`Status updated to '${newStatus}'`);
  } catch (err) {
    console.error("Status update failed:", err);
  }
};

window.handlePostJob = async function(event) {
  event.preventDefault();
  const form = event.target;
  const payload = {
    title: form.title.value,
    company: form.company.value,
    sector: form.sector.value,
    location: form.location.value,
    stipend_salary: form.stipend.value,
    required_skills: form.reqSkills.value.split(',').map(s => s.trim()).filter(Boolean),
    preferred_skills: form.prefSkills.value.split(',').map(s => s.trim()).filter(Boolean),
    description: form.description.value
  };

  try {
    const res = await fetch('/api/recruiter/jobs', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const created = await res.json();
    showToast("Job opportunity posted successfully!");
    form.reset();
    await loadJobs();
    state.selectedJobId = created.id;
    loadRecruiterCandidates(created.id);
  } catch (err) {
    alert("Error posting job: " + err.message);
  }
};

function renderTPOVisuals() {
  const data = state.tpoAnalytics;
  if (!data) return;

  document.getElementById('tpo-total-students').textContent = data.total_students;
  document.getElementById('tpo-ready-pct').textContent = `${data.placement_ready_pct}%`;
  document.getElementById('tpo-avg-readiness').textContent = `${data.avg_readiness}%`;

  // Render Heatmap Table
  const heatmapContainer = document.getElementById('tpo-heatmap-container');
  if (heatmapContainer && data.dept_heatmaps) {
    const depts = Object.keys(data.dept_heatmaps);
    const vectors = ["Web Dev", "Cloud & DevOps", "AI & Data Science", "Core CS", "Databases"];

    let html = `
      <table class="w-full text-xs text-left border border-slate-200 rounded-lg overflow-hidden">
        <thead class="bg-slate-100 text-slate-700 font-semibold">
          <tr>
            <th class="p-2.5">Department</th>
            ${vectors.map(v => `<th class="p-2.5 text-center">${v}</th>`).join('')}
          </tr>
        </thead>
        <tbody>
    `;

    depts.forEach(d => {
      html += `<tr class="border-t border-slate-100"><td class="p-2.5 font-bold text-slate-800">${d}</td>`;
      vectors.forEach(v => {
        const val = data.dept_heatmaps[d][v] || 0;
        let bg = 'bg-rose-50 text-rose-700';
        if (val >= 75) bg = 'bg-emerald-100 text-emerald-800';
        else if (val >= 50) bg = 'bg-indigo-100 text-indigo-800';
        else if (val >= 30) bg = 'bg-amber-100 text-amber-800';

        html += `<td class="p-2.5 text-center"><span class="px-2 py-1 rounded font-semibold heatmap-cell ${bg}">${val}%</span></td>`;
      });
      html += `</tr>`;
    });

    html += `</tbody></table>`;
    heatmapContainer.innerHTML = html;
  }

  // Render Missing Skills Bar Chart
  const chartCanvas = document.getElementById('tpoBarChartCanvas');
  if (chartCanvas && data.top_missing_skills) {
    if (state.tpoChartInstance) state.tpoChartInstance.destroy();

    const topSkills = data.top_missing_skills.slice(0, 6);
    const ctx = chartCanvas.getContext('2d');
    state.tpoChartInstance = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: topSkills.map(s => s.skill),
        datasets: [{
          label: '% Students Lacking Skill',
          data: topSkills.map(s => s.missing_percentage),
          backgroundColor: '#f87171',
          borderRadius: 6
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: { min: 0, max: 100, ticks: { callback: v => v + '%' } }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });
  }
}

window.exportTPOCSV = function() {
  window.location.href = '/api/tpo/export-csv';
};

// ==========================================
// 6. EVENT LISTENERS & HELPERS
// ==========================================

function setupUploadHandlers() {
  const dropArea = document.getElementById('resume-drop-zone');
  const fileInput = document.getElementById('resume-file-input');

  if (dropArea && fileInput) {
    dropArea.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', (e) => {
      if (e.target.files.length > 0) uploadPdfFile(e.target.files[0]);
    });

    ['dragenter', 'dragover'].forEach(name => {
      dropArea.addEventListener(name, (e) => {
        e.preventDefault();
        dropArea.classList.add('border-indigo-500', 'bg-indigo-50');
      });
    });

    ['dragleave', 'drop'].forEach(name => {
      dropArea.addEventListener(name, (e) => {
        e.preventDefault();
        dropArea.classList.remove('border-indigo-500', 'bg-indigo-50');
      });
    });

    dropArea.addEventListener('drop', (e) => {
      if (e.dataTransfer.files.length > 0) {
        uploadPdfFile(e.dataTransfer.files[0]);
      }
    });
  }
}

function showLoader(visible) {
  const loader = document.getElementById('global-loader');
  if (loader) loader.classList.toggle('hidden', !visible);
}

function showToast(msg) {
  const toast = document.getElementById('toast-notification');
  const text = document.getElementById('toast-text');
  if (toast && text) {
    text.textContent = msg;
    toast.classList.remove('hidden');
    setTimeout(() => toast.classList.add('hidden'), 3500);
  }
}
