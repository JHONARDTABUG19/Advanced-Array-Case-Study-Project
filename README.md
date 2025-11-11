<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Academic Analytics Lite</title>
</head>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">

  <!-- Title -->
  <h1 style="color: #ff6600; text-align: center;">🎓 Academic Analytics Lite</h1>
  <p style="text-align:center; font-size:16px;">
    A <b>Python-based program</b> that handles <b>data ingestion, validation, CRUD operations</b>, 
    and detailed <b>grade analytics & reporting</b> using a Text-based User Interface (TUI).
  </p>

  <!-- Features -->
  <h2 style="color: #007acc;">✨ Features</h2>
  <div style="border-left:5px solid #007acc; padding-left:10px;">
    <h3>🗂️ Data Management</h3>
    <ul>
      <li>➕ Add/Save Students – Insert new students into the records.</li>
      <li>📖 Read/Display – View the current contents of the student record file.</li>
      <li>❌ Delete by ID – Remove a specific student by ID.</li>
      <li>🔢 Sort Data – Sort the dataset based on any column.</li>
    </ul>

    <h3>📊 Grade Analysis</h3>
    <ul>
      <li>📈 Weighted Grade Computation – Calculate weighted grades for each student.</li>
      <li>📊 Grade Distribution – Analyze grade frequency (A–F).</li>
      <li>🏆 Percentiles – Identify top and bottom 10% students.</li>
      <li>📉 Improvement Tracking – Compare Final vs Midterm performance.</li>
    </ul>
  </div>

  <!-- File Structure -->
  <h2 style="color: #007acc;">🗃️ File Structure</h2>
  <table style="width:100%; border-collapse: collapse;">
    <thead>
      <tr style="background-color:#f0f8ff;">
        <th style="border:1px solid #ddd; padding:8px; text-align:left;">File Name</th>
        <th style="border:1px solid #ddd; padding:8px; text-align:left;">Description</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="border:1px solid #ddd; padding:8px;">main.py</td>
        <td style="border:1px solid #ddd; padding:8px;">Menu and user input handling, calls functions from other modules.</td>
      </tr>
      <tr style="background-color:#f9f9f9;">
        <td style="border:1px solid #ddd; padding:8px;">ingest.py</td>
        <td style="border:1px solid #ddd; padding:8px;">`clean_ingest`: Reads studentRecord.csv, validates data, checks ranges (0–100), handles missing values.</td>
      </tr>
      <tr>
        <td style="border:1px solid #ddd; padding:8px;">array_operations.py</td>
        <td style="border:1px solid #ddd; padding:8px;">Data manipulation: saving, deleting, selecting, projecting, sorting datasets.</td>
      </tr>
      <tr style="background-color:#f9f9f9;">
        <td style="border:1px solid #ddd; padding:8px;">analytics.py</td>
        <td style="border:1px solid #ddd; padding:8px;">Weighted averages and improvement tracking functions.</td>
      </tr>
      <tr>
        <td style="border:1px solid #ddd; padding:8px;">reportz.py</td>
        <td style="border:1px solid #ddd; padding:8px;">Generate summary reports, export at-risk student list, display section-specific data.</td>
      </tr>
      <tr style="background-color:#f9f9f9;">
        <td style="border:1px solid #ddd; padding:8px;">studentRecord.csv</td>
        <td style="border:1px solid #ddd; padding:8px;">CSV file containing student records.</td>
      </tr>
    </tbody>
  </table>

  <!-- Prerequisites -->
  <h2 style="color: #007acc;">🛠️ Prerequisites</h2>
  <div style="border:2px solid #007acc; padding:15px; border-radius:10px; background-color:#f0f8ff;">
    <p>Python 3.6+ is required.</p>
    <p>Install dependencies:</p>
    <pre style="background-color:#e0e0e0; padding:8px;">pip install numpy termcolor</pre>
    <p><b>Libraries:</b></p>
    <ul>
      <li><b>numpy</b> → for analytics and calculations</li>
      <li><b>termcolor</b> → for colored text output in the terminal</li>
    </ul>
  </div>

  <!-- How to Run -->
  <h2 style="color: #007acc;">▶️ How to Run</h2>
  <ol>
    <li>Ensure all Python files and <code>studentRecord.csv</code> are in the same directory.</li>
    <li>Open your terminal in that directory.</li>
    <li>Run the program: <pre style="background-color:#e0e0e0; padding:8px;">python main.py</pre></li>
    <li>Follow the on-screen menu prompts to interact with the system.</li>
  </ol>

  <!-- AI Use Disclosure -->
  <h2 style="color:#007acc;">🤖 AI Use Disclosure</h2>
  <p>
    Portions of this script were generated or refined using <b>ChatGPT</b> for debugging, grammar corrections, and optimization. 
    All AI outputs were <b>verified, tested, and modified by the author</b>.
  </p>

</body>
</html>
