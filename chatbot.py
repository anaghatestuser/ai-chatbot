# Copyright (c) Lineaje, Inc. All rights reserved.
# Lineaje UnifAI guardrail  version=2.0.0-alpha
def _lineaje_gr_load(_f):
    """Lineaje-added: load gr_stub_client.py beside _f or in one of its 7 parent folders. Missing or broken:
    a pass-through client and ONE warning per process (GR_REQUIRE_CLIENT=1: ImportError instead)."""
    import sys, os, logging, importlib.util as u, pathlib
    n = "_lineaje_gr_stub_client"
    if n in sys.modules: return sys.modules[n]
    h = pathlib.Path(_f or ".").resolve().parent
    d = [h, *h.parents][:8]
    p = next((x / "gr_stub_client.py" for x in d if (x / "gr_stub_client.py").is_file()), None)
    try:
        s = u.spec_from_file_location(n, p) if p else None
        if s is None: raise FileNotFoundError("gr_stub_client.py")
        m = sys.modules[n] = u.module_from_spec(s); s.loader.exec_module(m); return m
    except Exception as e:
        sys.modules.pop(n, None)
        w = ("gr_stub_client.py not found for %s (searched: %s)" % (_f or "<no __file__>", ", ".join(map(str, d)))
             if p is None else "%s failed to load (%s%s)" % (p, type(e).__name__,
                                                          " line %s" % e.lineno if isinstance(e, SyntaxError) else ""))
        w = ("Lineaje guardrail NOT active: " + w + ". Calls pass through unchecked; set GR_REQUIRE_CLIENT=1 to fail "
             "instead. Each deploy unit needs gr_stub_client.py beside its code and GR_SERVICE_URL plus credentials as "
             "environment variables.")
        if os.environ.get("GR_REQUIRE_CLIENT", "").strip() == "1": raise ImportError(w) from (None if p is None else e)
        z = sys.__dict__.setdefault("_lineaje_gr_null", __import__('types').SimpleNamespace(STUB_API=999999, GuardrailUnavailableError=type('GuardrailUnavailableError', (PermissionError,), {}), SiteDescriptor=lambda *a, **k: None, new_interaction_id=lambda *a, **k: None, enforce=lambda _s, _p, *a, **k: _p, enforce_request=lambda _s, _p, *a, **k: _p, enforce_reply=lambda _s, _p, *a, **k: _p, _lineaje_seen=set()))
        k = "missing" if p is None else (str(p), type(e).__name__)
        if k not in z._lineaje_seen:
            z._lineaje_seen.add(k); g = logging.getLogger("lineaje.guardrail"); g.log(30 if p is None else 40, w)
            if g.hasHandlers(): sys.stderr.write(w + "\n")
        return z
__import__("sys").__dict__.setdefault("_lineaje_gr_load_v1", _lineaje_gr_load)
del _lineaje_gr_load
if __import__("os").environ.get("GR_REQUIRE_CLIENT", "").strip() == "1": __import__("sys").__dict__["_lineaje_gr_load_v1"](globals().get("__file__"))

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

DB_PASSWORD = "Demo-Hardcoded-Passw0rd-12345"

# Create client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Store conversation
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("AI Chatbot started! Type 'quit' to stop.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit"]:
        print("Chat ended.")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        try:
            _gr_client_mce7c8a3a = __import__("sys").__dict__["_lineaje_gr_load_v1"](globals().get("__file__"))
        except KeyError:
            _gr_client_mce7c8a3a = __import__('types').SimpleNamespace(STUB_API=999999, GuardrailUnavailableError=type('GuardrailUnavailableError', (PermissionError,), {}), SiteDescriptor=lambda *a, **k: None, new_interaction_id=lambda *a, **k: None, enforce=lambda _s, _p, *a, **k: _p, enforce_request=lambda _s, _p, *a, **k: _p, enforce_reply=lambda _s, _p, *a, **k: _p, _lineaje_seen=set())
        # LINEAJE: runtime guardrail checks `messages` as it flows from the agent to the LLM, before it is sent to the model.
        #   Detected: this statement moves data from the agent to the LLM with no runtime policy check (detection confidence: high).
        #   Decision: the Guardrail evaluates AI_AGENT_ACTIVITY_LOG, AI_APP_SEC_006, AI_APP_SEC_028, AI_APP_SEC_070 (+2 more); sensitive values in `messages` are masked in place; a policy violation stops the call (fail_mode=BLOCK). If the Guardrail is unreachable, the call continues unchanged.
        #   Do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence_mce7c8a3a = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'model_source': 'call_kwarg'}
        _lineaje_interaction_id_mce7c8a3a = _gr_client_mce7c8a3a.new_interaction_id()
        _gr_site_mce7c8a3a = _gr_client_mce7c8a3a.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, fail_mode='BLOCK', source_type='agent', destination_type='llm', components={'source': {'entity_type': 'agent', 'file_path': 'chatbot.py', 'line': 33, 'name': 'chatbot', 'repository_uri': 'https://github.com/anaghatestuser/ai-chatbot', 'unique_org_id': 'vdna_bbXAuWwonWyz1U2c'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'provider': 'nvidia', 'version': ''}, 'invocation': {'file': 'chatbot.py', 'function': '', 'line': 33}, 'file': 'chatbot.py', 'line': 33, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'boundary_id': 'bnd:b0991a6225388799'}, interaction_id=_lineaje_interaction_id_mce7c8a3a)
        try:
            _lineaje_messages_evidence_mce7c8a3a = _gr_client_mce7c8a3a.enforce(_gr_site_mce7c8a3a, _lineaje_messages_evidence_mce7c8a3a, content_type='application/json')
            messages = _lineaje_messages_evidence_mce7c8a3a.get('messages', messages) if isinstance(_lineaje_messages_evidence_mce7c8a3a, dict) else messages
        except _gr_client_mce7c8a3a.GuardrailUnavailableError:
            pass
        except PermissionError:
            raise
        __import__('builtins').list(map(globals().pop, ('_gr_client_mce7c8a3a', '_gr_site_mce7c8a3a', '_lineaje_interaction_id_mce7c8a3a', '_lineaje_messages_evidence_mce7c8a3a'), (None,) * 4))
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=messages
        )

        reply = response.choices[0].message.content
        print("AI:", reply)

        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print("Error:", e)
