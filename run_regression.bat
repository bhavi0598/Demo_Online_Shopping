@echo off
echo Running all tests in parallel batches...
REM Run pytest with 3 parallel threads, generating a detailed HTML report
pytest -v -s tests/ --html=reports/summary_report.html --self-contained-html -n 3

REM Output a message after tests complete
echo All tests executed and report generated in 'Reports/final_report.html'
pause
