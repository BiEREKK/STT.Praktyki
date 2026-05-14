# Projekt: System Transkrypcji Mowy (STT) z użyciem OpenAI Whisper

## 🎯 Cel projektu
Stworzenie pełnoekranowej aplikacji webowej umożliwiającej nagrywanie dźwięku w czasie rzeczywistym przez przeglądarkę, przesyłanie go do serwera i generowanie transkrypcji tekstowej przy użyciu modelu **OpenAI Whisper**.

---

## 🛠 Wymagania Techniczne (Stack)
- **Backend:** Python (FastAPI lub Flask)
- **Model AI:** Biblioteka `openai-whisper`
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla JS lub React/Vue)
- **Inne:** `ffmpeg` zainstalowany w systemie operacyjnym (wymagany przez Whisper)

---

## 📋 Lista zadań do wykonania

### Etap 1: Przygotowanie Środowiska (Backend)
- [ ] **Zadanie 1.1:** Konfiguracja wirtualnego środowiska Pythona (`venv`).
- [ ] **Zadanie 1.2:** Instalacja zależności: `fastapi`, `uvicorn`, `openai-whisper`, `python-multipart`.
- [ ] **Zadanie 1.3:** Weryfikacja poprawności instalacji narzędzia `ffmpeg` w systemie.

### Etap 2: Logika Serwera i API
- [ ] **Zadanie 2.1:** Inicjalizacja modelu Whisper podczas startu aplikacji (ładowanie globalne, aby uniknąć przeładowywania przy każdym zapytaniu).
- [ ] **Zadanie 2.2:** Stworzenie endpointu `POST /transcribe`, który przyjmuje plik audio jako `UploadFile`.
- [ ] **Zadanie 2.3:** Implementacja funkcji przetwarzania:
    - Zapis pliku tymczasowego na dysku.
    - Wywołanie `model.transcribe()`.
    - Zwrócenie wyniku w formacie JSON: `{ "text": "..." }`.
    - Usunięcie pliku tymczasowego po przetworzeniu.

### Etap 3: Interfejs Użytkownika (Frontend)
- [ ] **Zadanie 3.1:** Przygotowanie struktury HTML:
    - Przycisk "Rozpocznij nagrywanie" / "Zatrzymaj".
    - Wskaźnik stanu nagrywania (np. migająca dioda lub zmiana tekstu).
    - Kontener `<div>` lub `<textarea>` na wynikowy tekst.
- [ ] **Zadanie 3.2:** Implementacja nagrywania w JS (`MediaRecorder API`).
- [ ] **Zadanie 3.3:** Obsługa wysyłki danych:
    - Konwersja nagrania do formatu Blob.
    - Przesłanie pliku do API za pomocą `fetch()`.
    - Obsługa wyświetlania "loadera" (oczekiwanie na wynik).

### Etap 4: Funkcje Zaawansowane (Dla ambitnych)
- [ ] **Zadanie 4.1 (Konfiguracja):** Dodanie panelu ustawień na stronie:
    - Wybor modelu (np. `tiny`, `base`, `small`).
    - Wybór języka (lista języków lub "Auto-detection").
    - Wybór zadania (Transkrypcja vs Tłumaczenie na angielski).
- [ ] **Zadanie 4.2 (Parametry API):** Przesyłanie wybranych parametrów z frontendu do backendu i uwzględnienie ich w wywołaniu modelu Whisper.
- [ ] **Zadanie 4.3 (UI/UX):** Dodanie wizualizacji fali dźwiękowej (Visualizer) podczas nagrywania.

---

## 🏁 Kryteria Oceny
1. **Poprawność:** Czy system generuje poprawny tekst na podstawie nagrania?
2. **Stabilność:** Czy aplikacja radzi sobie z błędami (np. brak mikrofonu, błąd serwera)?
3. **Architektura:** Czy model jest ładowany efektywnie (raz), a nie przy każdym żądaniu?
4. **Interfejs:** Czy obsługa jest intuicyjna i czy użytkownik widzi status przetwarzania?

---

## 💡 Podpowiedź dla studentów
Podczas nagrywania w Chrome/Firefox, domyślnym formatem jest często `audio/webm`. Whisper zazwyczaj radzi sobie z nim bezpośrednio, jeśli w systemie jest `ffmpeg`. Jeśli wystąpią błędy formatu, rozważ użycie biblioteki `pydub` do konwersji wewnątrz Pythona.

---

## Przykład wywołania modelu w backendzie
```
import whisper

model = whisper.load_model("base")
result = model.transcribe("audio_file.wav", language="pl", task="transcribe")
print(result["text"])
```