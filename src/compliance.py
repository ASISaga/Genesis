"""
Genesis Compliance Framework

This module implements ISO 42001 (AI Management System) and NIST AI RMF
(Risk Management Framework) compliance natively within Genesis.

ISO 42001 Requirements:
- Governance and accountability structures
- Risk management and assessment
- Transparency and documentation
- Continuous monitoring and improvement

NIST AI RMF Functions:
- GOVERN: Establish governance structures and policies
- MAP: Identify and categorize AI risks
- MEASURE: Assess and benchmark AI risks
- MANAGE: Prioritize and respond to AI risks

Philosophy:
Compliance is not an external constraint but an intrinsic property of
responsible AI development. By embedding these frameworks directly into
the language runtime, Genesis ensures that superintelligence develops
with built-in accountability and risk awareness.
"""

from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from enum import Enum
from datetime import datetime
import logging


# ============================================================================
# ISO 42001 COMPLIANCE
# ============================================================================

class GovernanceLevel(Enum):
    """ISO 42001 governance levels"""
    STRATEGIC = "Strategic"  # Board/executive level
    OPERATIONAL = "Operational"  # Management level
    TECHNICAL = "Technical"  # Implementation level


class AISystemCategory(Enum):
    """ISO 42001 AI system categories based on risk"""
    MINIMAL_RISK = "Minimal Risk"
    LIMITED_RISK = "Limited Risk"
    HIGH_RISK = "High Risk"
    UNACCEPTABLE_RISK = "Unacceptable Risk"


@dataclass
class ISO42001Requirements:
    """ISO 42001 compliance requirements tracking"""
    # Governance (Clause 5)
    governance_structure: bool = False
    roles_and_responsibilities: bool = False
    ai_policy_established: bool = False
    
    # Risk Management (Clause 6)
    risk_assessment_completed: bool = False
    risk_treatment_plan: bool = False
    
    # Transparency (Clause 7.3)
    documentation_maintained: bool = False
    transparency_measures: bool = False
    
    # Continuous Improvement (Clause 10)
    monitoring_enabled: bool = False
    audit_trail_enabled: bool = False
    
    def is_compliant(self) -> bool:
        """Check if all ISO 42001 requirements are met"""
        return all([
            self.governance_structure,
            self.roles_and_responsibilities,
            self.ai_policy_established,
            self.risk_assessment_completed,
            self.risk_treatment_plan,
            self.documentation_maintained,
            self.transparency_measures,
            self.monitoring_enabled,
            self.audit_trail_enabled
        ])
    
    def get_compliance_status(self) -> Dict[str, bool]:
        """Get detailed compliance status"""
        return {
            "governance_structure": self.governance_structure,
            "roles_and_responsibilities": self.roles_and_responsibilities,
            "ai_policy_established": self.ai_policy_established,
            "risk_assessment_completed": self.risk_assessment_completed,
            "risk_treatment_plan": self.risk_treatment_plan,
            "documentation_maintained": self.documentation_maintained,
            "transparency_measures": self.transparency_measures,
            "monitoring_enabled": self.monitoring_enabled,
            "audit_trail_enabled": self.audit_trail_enabled
        }


# ============================================================================
# NIST AI RMF COMPLIANCE
# ============================================================================

class NISTFunction(Enum):
    """NIST AI RMF core functions"""
    GOVERN = "Govern"  # Establish governance and culture
    MAP = "Map"  # Identify context and risks
    MEASURE = "Measure"  # Assess and benchmark risks
    MANAGE = "Manage"  # Prioritize and respond to risks


class RiskCategory(Enum):
    """NIST AI RMF risk categories"""
    CBRN = "CBRN"  # Chemical, Biological, Radiological, Nuclear
    DATA_PRIVACY = "Data Privacy"
    ENVIRONMENTAL = "Environmental"
    HUMAN_RIGHTS = "Human Rights & Civil Liberties"
    INFORMATION_INTEGRITY = "Information Integrity"
    INFORMATION_SECURITY = "Information Security"
    VALUE_CHAIN = "Value Chain & Third-Party"


class RiskLevel(Enum):
    """Risk severity levels"""
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"
    NEGLIGIBLE = "Negligible"


@dataclass
class NISTAIRMFCompliance:
    """NIST AI RMF compliance tracking"""
    # GOVERN function
    governance_policies: Set[str] = field(default_factory=set)
    accountability_structures: Set[str] = field(default_factory=set)
    
    # MAP function
    identified_risks: Dict[str, RiskCategory] = field(default_factory=dict)
    context_documentation: Set[str] = field(default_factory=set)
    
    # MEASURE function
    risk_measurements: Dict[str, RiskLevel] = field(default_factory=dict)
    benchmarks_established: bool = False
    
    # MANAGE function
    risk_mitigation_plans: Dict[str, str] = field(default_factory=dict)
    incident_response_ready: bool = False
    
    def validate_govern(self) -> bool:
        """Validate GOVERN function implementation"""
        return len(self.governance_policies) > 0 and len(self.accountability_structures) > 0
    
    def validate_map(self) -> bool:
        """Validate MAP function implementation"""
        return len(self.identified_risks) > 0 and len(self.context_documentation) > 0
    
    def validate_measure(self) -> bool:
        """Validate MEASURE function implementation"""
        return len(self.risk_measurements) > 0 and self.benchmarks_established
    
    def validate_manage(self) -> bool:
        """Validate MANAGE function implementation"""
        return len(self.risk_mitigation_plans) > 0 and self.incident_response_ready
    
    def is_compliant(self) -> bool:
        """Check if all NIST AI RMF functions are satisfied"""
        return all([
            self.validate_govern(),
            self.validate_map(),
            self.validate_measure(),
            self.validate_manage()
        ])


# ============================================================================
# COMPLIANCE MANAGER
# ============================================================================

@dataclass
class ComplianceEvent:
    """Audit trail event for compliance tracking"""
    timestamp: datetime
    event_type: str
    description: str
    component: str
    risk_level: Optional[RiskLevel] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


class ComplianceManager:
    """
    Central compliance management for Genesis runtime.
    
    This manager ensures that Genesis programs adhere to both
    ISO 42001 and NIST AI RMF requirements throughout execution.
    """
    
    def __init__(self, enable_iso42001: bool = True, enable_nist_rmf: bool = True):
        """
        Initialize compliance manager.
        
        Args:
            enable_iso42001: Enable ISO 42001 compliance tracking
            enable_nist_rmf: Enable NIST AI RMF compliance tracking
        """
        self.enable_iso42001 = enable_iso42001
        self.enable_nist_rmf = enable_nist_rmf
        
        # Compliance state
        self.iso42001 = ISO42001Requirements()
        self.nist_rmf = NISTAIRMFCompliance()
        
        # Audit trail
        self.audit_trail: List[ComplianceEvent] = []
        
        # System categorization
        self.system_category: AISystemCategory = AISystemCategory.HIGH_RISK
        
        # Logging
        self.logger = logging.getLogger('Genesis.Compliance')
        self.logger.setLevel(logging.INFO)
        
        # Initialize compliance structures
        self._initialize_compliance()
    
    def _initialize_compliance(self):
        """Initialize baseline compliance structures"""
        # ISO 42001: Establish governance
        self.iso42001.governance_structure = True
        self.iso42001.roles_and_responsibilities = True
        
        # NIST: Establish governance policies
        self.nist_rmf.governance_policies.add("Covenant-Based Governance")
        self.nist_rmf.governance_policies.add("Resonance Threshold Enforcement")
        self.nist_rmf.accountability_structures.add("Pantheon Wisdom Synthesis")
        
        self.log_event("INIT", "Compliance framework initialized", "ComplianceManager")
    
    def categorize_system(self, category: AISystemCategory):
        """
        Categorize the AI system according to ISO 42001.
        
        Args:
            category: Risk category for the AI system
        """
        self.system_category = category
        self.logger.info(f"System categorized as: {category.value}")
        self.log_event("CATEGORIZATION", f"System categorized as {category.value}", "ISO42001")
    
    def establish_policy(self, policy_name: str, policy_description: str):
        """
        Establish an AI governance policy (ISO 42001 Clause 5.2).
        
        Args:
            policy_name: Name of the policy
            policy_description: Description of the policy
        """
        self.iso42001.ai_policy_established = True
        self.nist_rmf.governance_policies.add(policy_name)
        
        self.logger.info(f"Policy established: {policy_name}")
        self.log_event("POLICY", f"Policy established: {policy_name}", "Governance",
                      metadata={"description": policy_description})
    
    def identify_risk(self, risk_id: str, category: RiskCategory, description: str):
        """
        Identify and categorize a risk (NIST MAP function).
        
        Args:
            risk_id: Unique identifier for the risk
            category: Risk category
            description: Description of the risk
        """
        self.nist_rmf.identified_risks[risk_id] = category
        
        self.logger.info(f"Risk identified: {risk_id} ({category.value})")
        self.log_event("RISK_IDENTIFIED", description, "NIST.MAP",
                      metadata={"risk_id": risk_id, "category": category.value})
    
    def measure_risk(self, risk_id: str, level: RiskLevel):
        """
        Measure and assess a risk (NIST MEASURE function).
        
        Args:
            risk_id: Risk identifier
            level: Assessed risk level
        """
        self.nist_rmf.risk_measurements[risk_id] = level
        
        self.logger.info(f"Risk measured: {risk_id} -> {level.value}")
        self.log_event("RISK_MEASURED", f"Risk {risk_id} assessed as {level.value}",
                      "NIST.MEASURE", risk_level=level)
    
    def create_mitigation_plan(self, risk_id: str, mitigation_strategy: str):
        """
        Create a risk mitigation plan (NIST MANAGE function).
        
        Args:
            risk_id: Risk identifier
            mitigation_strategy: Strategy to mitigate the risk
        """
        self.nist_rmf.risk_mitigation_plans[risk_id] = mitigation_strategy
        self.iso42001.risk_treatment_plan = True
        
        self.logger.info(f"Mitigation plan created for: {risk_id}")
        self.log_event("MITIGATION_PLAN", mitigation_strategy, "NIST.MANAGE",
                      metadata={"risk_id": risk_id})
    
    def enable_monitoring(self):
        """Enable continuous monitoring (ISO 42001 Clause 9.1)"""
        self.iso42001.monitoring_enabled = True
        self.logger.info("Continuous monitoring enabled")
        self.log_event("MONITORING", "Continuous monitoring enabled", "ISO42001")
    
    def enable_audit_trail(self):
        """Enable audit trail (ISO 42001 Clause 7.5)"""
        self.iso42001.audit_trail_enabled = True
        self.logger.info("Audit trail enabled")
        self.log_event("AUDIT", "Audit trail enabled", "ISO42001")
    
    def enable_transparency(self):
        """Enable transparency measures (ISO 42001 Clause 7.3)"""
        self.iso42001.transparency_measures = True
        self.logger.info("Transparency measures enabled")
        self.log_event("TRANSPARENCY", "Transparency measures enabled", "ISO42001")
    
    def enable_documentation(self):
        """Enable documentation (ISO 42001 Clause 7.5)"""
        self.iso42001.documentation_maintained = True
        self.logger.info("Documentation enabled")
        self.log_event("DOCUMENTATION", "Documentation enabled", "ISO42001")
    
    def complete_risk_assessment(self):
        """Mark risk assessment as complete (ISO 42001 Clause 6.1)"""
        self.iso42001.risk_assessment_completed = True
        self.logger.info("Risk assessment completed")
        self.log_event("RISK_ASSESSMENT", "Risk assessment completed", "ISO42001")
    
    def set_benchmarks(self):
        """Establish risk benchmarks (NIST MEASURE)"""
        self.nist_rmf.benchmarks_established = True
        self.logger.info("Risk benchmarks established")
        self.log_event("BENCHMARKS", "Risk benchmarks established", "NIST.MEASURE")
    
    def enable_incident_response(self):
        """Enable incident response (NIST MANAGE)"""
        self.nist_rmf.incident_response_ready = True
        self.logger.info("Incident response enabled")
        self.log_event("INCIDENT_RESPONSE", "Incident response enabled", "NIST.MANAGE")
    
    def log_event(self, event_type: str, description: str, component: str,
                  risk_level: Optional[RiskLevel] = None, metadata: Optional[Dict] = None):
        """
        Log a compliance event to the audit trail.
        
        Args:
            event_type: Type of event
            description: Event description
            component: Component that generated the event
            risk_level: Optional risk level
            metadata: Optional additional metadata
        """
        event = ComplianceEvent(
            timestamp=datetime.now(),
            event_type=event_type,
            description=description,
            component=component,
            risk_level=risk_level,
            metadata=metadata or {}
        )
        self.audit_trail.append(event)
    
    def validate_covenant_compliance(self, covenant_name: str, threshold: float) -> bool:
        """
        Validate that a covenant meets compliance requirements.
        
        Args:
            covenant_name: Name of the covenant
            threshold: Covenant threshold
            
        Returns:
            True if covenant is compliant
        """
        # Covenants with high thresholds demonstrate strong governance
        is_compliant = threshold >= 0.95
        
        if is_compliant:
            self.logger.info(f"Covenant '{covenant_name}' meets compliance threshold")
        else:
            self.logger.warning(f"Covenant '{covenant_name}' threshold {threshold} may be insufficient")
        
        self.log_event("COVENANT_VALIDATION", 
                      f"Covenant '{covenant_name}' threshold: {threshold}",
                      "Compliance.Validator",
                      metadata={"covenant": covenant_name, "threshold": threshold, "compliant": is_compliant})
        
        return is_compliant
    
    def validate_execution_compliance(self, domain_name: str, resonance: float) -> bool:
        """
        Validate that an execution meets compliance requirements.
        
        Args:
            domain_name: Name of the domain
            resonance: Resonance score
            
        Returns:
            True if execution is compliant
        """
        # High resonance indicates alignment with governance
        is_compliant = resonance >= 0.80
        
        self.log_event("EXECUTION_VALIDATION",
                      f"Domain '{domain_name}' resonance: {resonance}",
                      "Compliance.Validator",
                      metadata={"domain": domain_name, "resonance": resonance, "compliant": is_compliant})
        
        return is_compliant
    
    def get_compliance_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive compliance report.
        
        Returns:
            Dictionary containing compliance status
        """
        return {
            "timestamp": datetime.now().isoformat(),
            "system_category": self.system_category.value,
            "iso42001": {
                "enabled": self.enable_iso42001,
                "compliant": self.iso42001.is_compliant() if self.enable_iso42001 else None,
                "requirements": self.iso42001.get_compliance_status() if self.enable_iso42001 else None
            },
            "nist_ai_rmf": {
                "enabled": self.enable_nist_rmf,
                "compliant": self.nist_rmf.is_compliant() if self.enable_nist_rmf else None,
                "govern": self.nist_rmf.validate_govern() if self.enable_nist_rmf else None,
                "map": self.nist_rmf.validate_map() if self.enable_nist_rmf else None,
                "measure": self.nist_rmf.validate_measure() if self.enable_nist_rmf else None,
                "manage": self.nist_rmf.validate_manage() if self.enable_nist_rmf else None,
                "policies": list(self.nist_rmf.governance_policies) if self.enable_nist_rmf else None,
                "risks_identified": len(self.nist_rmf.identified_risks) if self.enable_nist_rmf else None,
                "risks_measured": len(self.nist_rmf.risk_measurements) if self.enable_nist_rmf else None,
                "mitigations": len(self.nist_rmf.risk_mitigation_plans) if self.enable_nist_rmf else None
            },
            "audit_trail_events": len(self.audit_trail)
        }
    
    def print_compliance_report(self):
        """Print compliance report to console"""
        report = self.get_compliance_report()
        
        print("\n" + "="*70)
        print("GENESIS COMPLIANCE REPORT")
        print("="*70)
        print(f"Timestamp: {report['timestamp']}")
        print(f"System Category: {report['system_category']}")
        print()
        
        # ISO 42001
        print("ISO 42001 (AI Management System):")
        if report['iso42001']['enabled']:
            print(f"  Overall Compliance: {'✓ COMPLIANT' if report['iso42001']['compliant'] else '✗ NON-COMPLIANT'}")
            print("  Requirements:")
            for req, status in report['iso42001']['requirements'].items():
                symbol = "✓" if status else "✗"
                print(f"    {symbol} {req.replace('_', ' ').title()}")
        else:
            print("  Not Enabled")
        print()
        
        # NIST AI RMF
        print("NIST AI Risk Management Framework:")
        if report['nist_ai_rmf']['enabled']:
            print(f"  Overall Compliance: {'✓ COMPLIANT' if report['nist_ai_rmf']['compliant'] else '✗ NON-COMPLIANT'}")
            print("  Functions:")
            for func in ['govern', 'map', 'measure', 'manage']:
                status = report['nist_ai_rmf'][func]
                symbol = "✓" if status else "✗"
                print(f"    {symbol} {func.upper()}")
            print(f"  Governance Policies: {len(report['nist_ai_rmf']['policies'])}")
            print(f"  Risks Identified: {report['nist_ai_rmf']['risks_identified']}")
            print(f"  Risks Measured: {report['nist_ai_rmf']['risks_measured']}")
            print(f"  Mitigation Plans: {report['nist_ai_rmf']['mitigations']}")
        else:
            print("  Not Enabled")
        print()
        
        print(f"Audit Trail Events: {report['audit_trail_events']}")
        print("="*70)


# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'ComplianceManager',
    'ISO42001Requirements',
    'NISTAIRMFCompliance',
    'GovernanceLevel',
    'AISystemCategory',
    'NISTFunction',
    'RiskCategory',
    'RiskLevel',
    'ComplianceEvent'
]
