#!/usr/bin/env python3
"""
Basic test script to verify PUA skill structure and content.
"""

import os
import yaml

def test_skill_structure():
    """Test that the SKILL.md has proper structure."""
    skill_path = "SKILL.md"
    
    if not os.path.exists(skill_path):
        print("❌ SKILL.md not found")
        return False
    
    with open(skill_path, 'r') as f:
        content = f.read()
    
    # Check YAML frontmatter
    if not content.startswith('---'):
        print("❌ Missing YAML frontmatter")
        return False
    
    try:
        # Extract YAML frontmatter
        yaml_content = content.split('---')[1]
        metadata = yaml.safe_load(yaml_content)
        
        # Check required fields
        if 'name' not in metadata:
            print("❌ Missing 'name' in YAML frontmatter")
            return False
        
        if 'description' not in metadata:
            print("❌ Missing 'description' in YAML frontmatter")
            return False
        
        if metadata['name'] != 'pua':
            print(f"❌ Expected name 'pua', got '{metadata['name']}'")
            return False
        
        print("✅ YAML frontmatter is valid")
        
    except Exception as e:
        print(f"❌ Error parsing YAML frontmatter: {e}")
        return False
    
    # Check for key content sections
    required_sections = [
        "Trigger Conditions",
        "Three Iron Rules", 
        "Pressure Escalation",
        "Debugging Methodology"
    ]
    
    for section in required_sections:
        if section not in content:
            print(f"❌ Missing section: {section}")
            return False
    
    print("✅ All required sections present")
    return True

def test_trigger_conditions():
    """Test that trigger conditions are properly defined."""
    skill_path = "SKILL.md"
    
    with open(skill_path, 'r') as f:
        content = f.read()
    
    # Check for auto-trigger conditions
    auto_triggers = [
        "Task has failed 2+ times consecutively",
        "About to say \"I cannot\"",
        "Pushes the problem to user"
    ]
    
    for trigger in auto_triggers:
        if trigger not in content:
            print(f"❌ Missing auto-trigger condition: {trigger}")
            return False
    
    # Check for manual trigger
    if "/pua" not in content:
        print("❌ Missing manual trigger (/pua)")
        return False
    
    # Check for user frustration phrases
    frustration_phrases = [
        "why does this still not work",
        "try harder", 
        "you keep failing"
    ]
    
    for phrase in frustration_phrases:
        if phrase not in content:
            print(f"❌ Missing frustration phrase: {phrase}")
            return False
    
    print("✅ All trigger conditions present")
    return True

if __name__ == "__main__":
    print("🧪 Testing OpenClaw PUA Skill...")
    print()
    
    success = True
    success &= test_skill_structure()
    success &= test_trigger_conditions()
    
    print()
    if success:
        print("🎉 All tests passed! The PUA skill is ready for use.")
    else:
        print("❌ Some tests failed. Please check the skill file.")