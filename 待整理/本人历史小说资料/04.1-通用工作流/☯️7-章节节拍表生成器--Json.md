# ☯️7-章节节拍表生成器--Json

```json
{
  "_usage_instructions": {
    "description": "章节节拍表JSON结构化输出模板 - 使用说明",
    "how_to_use": [
      "1. 将此JSON模板作为输出格式参考",
      "2. 发送章节编号时，AI将按此结构生成节拍表",
      "3. 根据章节内容选择需要的节拍类型模板填充",
      "4. 【爽点密集区标注】嵌入在爽点最密集的节拍开头"
    ],
    "beat_types": {
      "scene_beat": "场景节拍 - 用于场景描写、情节推进",
      "dialogue_beat": "对话节拍 - 用于人物对话、信息传递",
      "combat_beat": "战斗节拍 - 用于打斗、对决场面",
      "reward_beat": "收获节拍 - 用于战利品清点、实力提升",
      "hook_beat": "悬念钩子节拍 - 用于章节结尾悬念"
    },
    "word_count_target": "每章2200-2500字",
    "excitement_density": "建议每章6-10个爽点"
  },

  "chapter_beat_sheet": {
    "header": {
      "chapter_number": "",
      "chapter_title": "",
      "core_conflict": "",
      "excitement_density": "",
      "word_count_target": "2200-2500字",
      "emotional_tone": "",
      "key_characters": []
    },
    "word_allocation_table": [],
    "total_words": "",
    "beats": []
  },

  "beat_templates": {
    "scene_beat": {
      "beat_number": "",
      "beat_name": "",
      "beat_type": "场景节拍",
      "scene_goal": "",
      "spacetime_positioning": {
        "time": "",
        "location": "",
        "characters_present": []
      },
      "plot_flow": {
        "opening_scene": {
          "description": "",
          "character_action": "",
          "environment_details": "",
          "psychological_state": ""
        },
        "conflict_ignition": {
          "description": "",
          "trigger_point": "",
          "opponent_reaction": "",
          "tension_escalation": ""
        },
        "excitement_release": {
          "description": "",
          "excitement_type": "",
          "specific_performance": "",
          "contrast_gap": "",
          "bystander_reaction": ""
        },
        "result_presentation": {
          "description": "",
          "protagonist_gains": "",
          "enemy_losses": "",
          "impact_range": ""
        }
      },
      "key_dialogues": {
        "protagonist_quote": "",
        "enemy_scene": "",
        "supporting_reaction": "",
        "inner_monologue": ""
      },
      "visual_focus": {
        "action_scene": "",
        "expression_details": "",
        "atmosphere_rendering": "",
        "contrast_shots": ""
      },
      "excitement_checklist": {
        "face_slapping": "",
        "power_crushing": "",
        "wealth_surge": "",
        "beauty_interaction": "",
        "crowd_shock": "",
        "enemy_death": ""
      },
      "rhythm_control": {
        "pace": "",
        "word_allocation": "",
        "tension_index": ""
      },
      "writing_notes": {
        "forbidden": [],
        "required": [],
        "emphasis": ""
      },
      "transition_hook": {
        "ending_suspense": "",
        "next_scene_guide": ""
      }
    },

    "dialogue_beat": {
      "beat_number": "",
      "beat_name": "",
      "beat_type": "对话节拍",
      "dialogue_goal": "",
      "dialogue_parties": {
        "party_a": {
          "name": "",
          "psychological_state": "",
          "purpose": ""
        },
        "party_b": {
          "name": "",
          "psychological_state": "",
          "purpose": ""
        }
      },
      "dialogue_flow": {
        "opening": {
          "first_speaker": "",
          "content": "",
          "tone": "",
          "action": ""
        },
        "exchange": [],
        "atmosphere_change": "",
        "climax_quotes": {
          "show_off_quote": "",
          "face_slap_response": ""
        },
        "ending": {
          "how_ended": "",
          "impact_left": ""
        }
      },
      "dialogue_embellishments": {
        "expression_description": "",
        "action_interspersed": "",
        "environment_backdrop": ""
      },
      "dialogue_style": {
        "protagonist": "",
        "enemy": "",
        "supporting": ""
      },
      "excitement_checklist": {
        "face_slapping": "",
        "power_crushing": "",
        "wealth_surge": "",
        "beauty_interaction": "",
        "crowd_shock": "",
        "enemy_death": ""
      },
      "rhythm_control": {
        "pace": "",
        "word_allocation": "",
        "tension_index": ""
      },
      "writing_notes": {
        "forbidden": [],
        "required": [],
        "emphasis": ""
      },
      "transition_hook": {
        "ending_suspense": "",
        "next_scene_guide": ""
      }
    },

    "combat_beat": {
      "beat_number": "",
      "beat_name": "",
      "beat_type": "战斗节拍",
      "combat_goal": "",
      "power_comparison": {
        "protagonist_power": {
          "level": "",
          "advantage": "",
          "disadvantage": ""
        },
        "enemy_power": {
          "level": "",
          "features": "",
          "trump_card": ""
        },
        "power_gap": ""
      },
      "combat_flow": {
        "phase_1_probe": {
          "word_count": "50-100字",
          "enemy_attack": {
            "technique_name": "",
            "effect_description": ""
          },
          "protagonist_response": "",
          "bystander_reaction": ""
        },
        "phase_2_escalation": {
          "word_count": "100-150字",
          "enemy_ultimate": "",
          "protagonist_counter": "",
          "scene_description": ""
        },
        "phase_3_crushing": {
          "word_count": "150-200字",
          "protagonist_burst": "",
          "crushing_process": "",
          "enemy_state": ""
        },
        "phase_4_finale": {
          "word_count": "50-80字",
          "killing_blow": "",
          "death_description": "",
          "spoils_display": ""
        }
      },
      "key_frames": [],
      "combat_effects_vocabulary": {
        "actions": [],
        "sounds": [],
        "effects": []
      },
      "combat_rhythm": {
        "total_words": "",
        "pace": "",
        "focus": ""
      },
      "excitement_embedding": {
        "show_off_lines": "",
        "instant_kill_shock": "",
        "crowd_exclaim": "",
        "enemy_despair": "",
        "war_spoils": ""
      },
      "excitement_checklist": {
        "face_slapping": "",
        "power_crushing": "",
        "wealth_surge": "",
        "beauty_interaction": "",
        "crowd_shock": "",
        "enemy_death": ""
      },
      "rhythm_control": {
        "pace": "",
        "word_allocation": "",
        "tension_index": ""
      },
      "writing_notes": {
        "forbidden": [],
        "required": [],
        "emphasis": ""
      },
      "transition_hook": {
        "ending_suspense": "",
        "next_scene_guide": ""
      }
    },

    "reward_beat": {
      "beat_number": "",
      "beat_name": "",
      "beat_type": "收获节拍",
      "harvest_list": {
        "spirit_stones": {
          "amount": "",
          "description": ""
        },
        "pills": [],
        "techniques": [],
        "artifacts": [],
        "special_items": []
      },
      "power_upgrade": {
        "cultivation_progress": "",
        "skill_mastery": "",
        "trump_card_increase": ""
      },
      "excitement_design": {
        "wealth_visualization": "",
        "before_after_contrast": "",
        "supporting_envy": ""
      },
      "interactions": {
        "xi_dialogue": "",
        "partner_distribution": ""
      },
      "description_focus": {
        "use_numbers": "",
        "visual_impact": "",
        "psychological_satisfaction": ""
      },
      "excitement_checklist": {
        "face_slapping": "",
        "power_crushing": "",
        "wealth_surge": "",
        "beauty_interaction": "",
        "crowd_shock": "",
        "enemy_death": ""
      },
      "rhythm_control": {
        "pace": "",
        "word_allocation": "",
        "tension_index": ""
      },
      "writing_notes": {
        "forbidden": [],
        "required": [],
        "emphasis": ""
      },
      "transition_hook": {
        "ending_suspense": "",
        "next_scene_guide": ""
      }
    },

    "hook_beat": {
      "beat_number": "",
      "beat_name": "",
      "beat_type": "悬念钩子节拍",
      "hook_type": {
        "new_enemy_appears": "",
        "crisis_warning": "",
        "treasure_summon": "",
        "conspiracy_revealed": "",
        "beauty_reaction": "",
        "faction_response": ""
      },
      "specific_design": {
        "suspense_scene": "",
        "open_question": "",
        "expectation_guide": ""
      },
      "ending_quote": "",
      "camera_language": {
        "close_up": "",
        "long_shot": "",
        "montage": ""
      },
      "emotion_retention": "",
      "excitement_checklist": {
        "face_slapping": "",
        "power_crushing": "",
        "wealth_surge": "",
        "beauty_interaction": "",
        "crowd_shock": "",
        "enemy_death": ""
      },
      "rhythm_control": {
        "pace": "",
        "word_allocation": "",
        "tension_index": ""
      },
      "writing_notes": {
        "forbidden": [],
        "required": [],
        "emphasis": ""
      },
      "transition_hook": {
        "ending_suspense": "",
        "next_scene_guide": ""
      }
    },

    "excitement_dense_zone": {
      "zone_marker": "🔥 爽点密集区标注",
      "consecutive_explosions": [],
      "crowd_reactions": [],
      "emotion_delivery": ""
    }
  },

  "quality_checklist": {
    "structural_integrity": {
      "scene_goals_clear": false,
      "story_unit_1_complete": {
        "name": "",
        "status": false
      },
      "story_unit_2_complete": {
        "name": "",
        "status": false
      },
      "scene_transitions_natural": false,
      "chapter_ending_strong": false
    },
    "excitement_distribution": {
      "total_count": 0,
      "excitement_types": [],
      "emotional_rhythm_alternating": false
    },
    "dialogue_design": {
      "xi_dialogue_count": 0,
      "xi_character_maintained": {
        "tsundere": false,
        "caring": false,
        "guiding": false,
        "rare_tenderness": false
      },
      "correct_address": "",
      "supporting_dialogue_rich": false
    },
    "visual_sense": {
      "scenes": []
    },
    "rhythm_control": {
      "opening": {
        "type": "",
        "description": ""
      },
      "middle": {
        "type": "",
        "description": ""
      },
      "ending": {
        "type": "",
        "description": ""
      },
      "tension_pacing": false
    },
    "character_consistency": {
      "protagonist": {
        "name": "",
        "traits": []
      },
      "xi": {
        "name": "",
        "traits": []
      },
      "supporting_characters": []
    },
    "special_requirements": {
      "volume_end_marker_clear": false,
      "next_volume_preview_attractive": false,
      "humanity_anchor_foreshadowed": false,
      "divine_blood_erosion_crisis_setup": false
    }
  },

  "_example_output": {
    "chapter_beat_sheet": {
      "header": {
        "chapter_number": "第1章",
        "chapter_title": "【觉醒】",
        "core_conflict": "主角神血觉醒，遭遇第一个敌人挑衅",
        "excitement_density": "8个爽点",
        "word_count_target": "2200-2500字",
        "emotional_tone": "热血/震撼",
        "key_characters": ["未启明", "曦", "杂鱼敌人A"]
      },
      "word_allocation_table": [
        {
          "beat_number": "#1",
          "beat_name": "神血苏醒",
          "beat_type": "场景节拍",
          "target_words": "400字",
          "tension_index": "★★★★☆"
        },
        {
          "beat_number": "#2",
          "beat_name": "与曦初对话",
          "beat_type": "对话节拍",
          "target_words": "350字",
          "tension_index": "★★★☆☆"
        },
        {
          "beat_number": "#3",
          "beat_name": "杂鱼挑衅",
          "beat_type": "场景节拍",
          "target_words": "300字",
          "tension_index": "★★★★☆"
        },
        {
          "beat_number": "#4",
          "beat_name": "碾压战斗",
          "beat_type": "战斗节拍",
          "target_words": "600字",
          "tension_index": "★★★★★"
        },
        {
          "beat_number": "#5",
          "beat_name": "战利品收获",
          "beat_type": "收获节拍",
          "target_words": "250字",
          "tension_index": "★★★☆☆"
        },
        {
          "beat_number": "#6",
          "beat_name": "神秘强敌窥视",
          "beat_type": "悬念钩子节拍",
          "target_words": "150字",
          "tension_index": "★★★★☆"
        }
      ],
      "total_words": "2050-2400字"
    }
  }
}
```
