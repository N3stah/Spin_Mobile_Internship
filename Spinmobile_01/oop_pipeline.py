"""
OOP Reporting Pipeline — SOLID Refactor of Week 3 CSV/JSON Parser
Spin Mobile Internship — Week 4 Assessment
Author: Mark Manoti Ndege
Date: September 2026

Description:
    An extensible, object-oriented reporting pipeline that reads transaction
    data from a source, calculates metrics, and writes a formatted report.
    Refactored from the Week 3 procedural csv_parser.py following SOLID
    design principles.
"""
from abc import ABC, abstractmethod
import json
