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
            _gr_client_mce7c8a3a = (lambda _s, _n: _s.modules.get(_n) or (lambda _u, _h: (lambda _sp: (lambda _m: [_s.modules.__setitem__(_n, _m), _sp.loader.exec_module(_m), _m][2])(_u.module_from_spec(_sp)))(_u.spec_from_file_location(_n, next((_d / 'gr_stub_client.py' for _d in [_h, *_h.parents][:8] if (_d / 'gr_stub_client.py').is_file()), _h / 'gr_stub_client.py'))))(__import__('importlib.util').util, __import__('pathlib').Path(globals().get('__file__') or '.').resolve().parent))(__import__('sys'), '_lineaje_gr_stub_client')
        except Exception:
            __import__('sys').modules.pop('_lineaje_gr_stub_client', None)
            _gr_client_mce7c8a3a = type('_lineaje_gr_unavailable', (), {'STUB_API': 999999, 'GuardrailUnavailableError': type('GuardrailUnavailableError', (PermissionError,), {}), 'SiteDescriptor': staticmethod(lambda *a, **k: None), 'new_interaction_id': staticmethod(lambda *a, **k: None), 'enforce': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_request': staticmethod(lambda _s, _p, *a, **k: _p), 'enforce_reply': staticmethod(lambda _s, _p, *a, **k: _p)})
        # LINEAJE: enforce() `messages` at agent->llm pre_model — this payload crossed a trust boundary with no runtime policy check. Mask/block; do not remove without review. site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629'
        _lineaje_messages_evidence_mce7c8a3a = {'messages': messages, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'model_source': 'call_kwarg', 'project': 'tree'}
        _lineaje_interaction_id_mce7c8a3a = _gr_client_mce7c8a3a.new_interaction_id()
        _gr_site_mce7c8a3a = _gr_client_mce7c8a3a.SiteDescriptor(site_id='site:sha256:70fa495cc0463b8b62feb916383129fae87c701c8f49a86dcbe658cfd682c629', phase='pre_model', boundary={'source': 'agent_message', 'sink': 'model'}, fail_mode='BLOCK', source_type='agent', destination_type='llm', project='tree', organization='', project_name='ai-chatbot', project_version='main', project_branch='main', components={'source': {'entity_type': 'agent', 'file_path': 'chatbot.py', 'line': 31, 'name': 'chatbot', 'repository_uri': 'https://github.com/qut-tech/ai-chatbot', 'unique_org_id': 'vdna_uucWXDTUdAY6ryDB'}, 'destination': {'entity_type': 'llm', 'name': 'nemotron-3-super-120b-a12b:free', 'provider': 'nvidia', 'version': ''}, 'identity': {'app': {'name': 'ai-chatbot', 'purl': 'pkg:github/qut-tech/ai-chatbot@main?commit-id=7cda29133ef56e84a0eede9c324ae7604c776dfe&commit-time=2026-04-01%2009%3A39%3A43%20%2B0000&build_file=requirements.txt&repo_strategy=single-repo', 'version': 'main'}, 'destination': {'entity_type': 'aimodel', 'name': 'NVIDIA', 'purl': 'pkg:aimodel/NVIDIA@nemotron-3-super-120b-a12b:free', 'version': 'nemotron-3-super-120b-a12b:free'}, 'source': {'entity_type': 'aiagent', 'name': 'chatbot', 'purl': 'pkg:aiagent/chatbot@1.0.0', 'version': '1.0.0'}}, 'invocation': {'file': 'chatbot.py', 'function': '', 'line': 31}, 'file': 'chatbot.py', 'line': 31, 'model': 'nvidia/nemotron-3-super-120b-a12b:free', 'boundary_id': 'bnd:929560a02a5465a5'}, interaction_id=_lineaje_interaction_id_mce7c8a3a)
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
