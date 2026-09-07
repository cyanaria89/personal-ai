# Data Fetching & REST API Integration Part09 - File Upload

---

# 1. File Upload Overview

## 1.1 File Upload 기본 개념

### [개념]

File Upload는 Frontend에서 사용자가 선택한 파일을 Backend API로 전송하는 Data Fetching 작업이다.

일반 JSON Request Body와 다르게 파일 업로드는 보통 `FormData`와 `multipart/form-data`를 사용한다.

Frontend Agent는 파일 선택, 파일 검증, 미리보기, FormData 생성, multipart 요청, 업로드 로딩, 업로드 실패 처리, 업로드 성공 후 UI 갱신 기준을 구분해야 한다.

기본 Flow:

```text
User Select File
→ Client File Validation
→ Preview Optional
→ Build FormData
→ multipart/form-data Request
→ Backend File Upload API
→ Response DTO
→ UI Update
```

---

### [핵심]

File Upload 핵심 키워드:

- File Upload
- FormData
- multipart/form-data
- File Input
- File Object
- Blob
- Image Upload
- Multiple Files
- Preview URL
- URL.createObjectURL
- URL.revokeObjectURL
- File Size Validation
- File Type Validation
- Extension Validation
- Upload Loading
- Upload Progress
- Axios Upload
- fetch Upload
- Request Body
- Content-Type Boundary
- Backend MultipartFile
- Response DTO

File Upload 목적:

- 사용자 이미지 업로드
- 프로필 이미지 업로드
- 리뷰 이미지 업로드
- 게시글 첨부파일 업로드
- 축제 이미지 업로드
- 채팅 이미지 업로드
- 파일 기반 데이터 전송

---

### [실무]

2026 실무 기준에서 File Upload는 JSON API와 분리해서 설계하는 것이 좋다.

실무 기준:

- 파일은 `FormData`로 전송
- JSON Request Body와 multipart request를 구분
- `Content-Type: multipart/form-data`를 수동으로 고정하지 않는 방식 권장
- 파일 크기와 확장자 검증
- 이미지 업로드는 preview 제공 가능
- preview URL은 사용 후 revoke
- 업로드 중 버튼 disabled 처리
- 업로드 실패 시 기존 입력값 유지
- 성공 후 응답 URL 또는 파일 id를 UI 상태에 반영
- 민감한 파일은 Backend 검증 필수
- Frontend 검증은 UX용이고 Backend 검증이 최종 기준

기본 예:

```typescript
const formData = new FormData();

formData.append("image", file);

await authApi.post("/reviews/images", formData);
```

---

### [FAQ]

Q. File Upload는 JSON으로 보내?
A. 일반적으로 파일은 JSON이 아니라 FormData와 multipart/form-data로 보낸다.

Q. FormData는 뭐야?
A. 파일과 텍스트 필드를 함께 전송할 수 있는 브라우저 API다.

Q. File Upload에서도 Axios를 쓸 수 있어?
A. 가능하다. Axios POST 요청의 body에 FormData를 넣어 전송할 수 있다.

Q. File Upload에서 가장 중요한 주의점은 뭐야?
A. FormData 사용, 파일 검증, 업로드 상태 처리, multipart Content-Type boundary 처리 기준이다.

---

# 2. File Input Rules

## 2.1 File Input 기본

### [개념]

File Input은 사용자가 로컬 파일을 선택할 수 있게 하는 HTML input이다.

Frontend는 `input[type="file"]`의 `files`에서 File 객체를 얻어 검증하고 업로드 요청에 사용한다.

---

### [핵심]

File Input 핵심 속성:

- type="file"
- accept
- multiple
- files
- FileList
- File
- name
- onChange
- disabled

File Input 사용 대상:

- 이미지 선택
- 첨부파일 선택
- 프로필 이미지 선택
- 여러 파일 선택
- 파일 업로드 Form

주의:

- input value로 파일 경로를 직접 다루지 않음
- `files`는 FileList
- 단일 파일은 `files[0]`
- 선택 취소 시 files가 비어 있을 수 있음
- accept는 UX 힌트이며 보안 검증 아님
- Backend에서도 파일 검증 필요

---

### [실무]

단일 파일 선택:

```tsx
function ImageInput() {
  const [file, setFile] = useState<File | null>(null);

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const selectedFile = event.target.files?.[0] ?? null;
    setFile(selectedFile);
  }

  return <input type="file" accept="image/*" onChange={handleChange} />;
}
```

다중 파일 선택:

```tsx
function MultipleImageInput() {
  const [files, setFiles] = useState<File[]>([]);

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const selectedFiles = Array.from(event.target.files ?? []);
    setFiles(selectedFiles);
  }

  return (
    <input type="file" accept="image/*" multiple onChange={handleChange} />
  );
}
```

주의:

- `event.target.files`가 null일 수 있음
- 같은 파일을 다시 선택해도 change 이벤트가 안 날 수 있음
- 필요 시 input value reset 처리
- accept만 믿지 말고 file.type과 file.name 검증
- 파일 선택 상태와 업로드 완료 상태를 구분

---

### [FAQ]

Q. File 객체는 어디서 얻어?
A. `input[type="file"]`의 `event.target.files`에서 얻는다.

Q. 단일 파일은 어떻게 가져와?
A. `event.target.files?.[0]`로 가져올 수 있다.

Q. multiple 속성은 언제 써?
A. 여러 파일을 한 번에 선택해야 할 때 사용한다.

Q. accept="image/\*"면 이미지 파일만 완전히 막을 수 있어?
A. 아니다. accept는 사용자 선택을 돕는 힌트이고 실제 검증은 Frontend와 Backend에서 따로 해야 한다.

---

# 3. FormData Rules

## 3.1 FormData 기본

### [개념]

FormData는 파일과 일반 문자열 필드를 multipart 요청으로 전송하기 위한 브라우저 API다.

File Upload API에서는 Request Body로 FormData를 사용한다.

---

### [핵심]

FormData 핵심 메서드:

- append
- set
- get
- getAll
- delete
- has

FormData에 넣는 값:

- File
- Blob
- string
- number as string
- JSON string
- multiple files

주의:

- number는 문자열로 변환될 수 있음
- 객체를 그대로 append하면 `[object Object]`가 될 수 있음
- JSON 객체는 `JSON.stringify` 후 append
- Backend field name과 append key 일치 필요
- multipart field name은 Backend `@RequestPart`, `@RequestParam` 기준 확인

---

### [실무]

단일 파일 FormData:

```typescript
const formData = new FormData();

formData.append("image", file);
```

파일 + 텍스트 필드:

```typescript
const formData = new FormData();

formData.append("image", file);
formData.append("festivalId", String(festivalId));
formData.append("content", content);
```

여러 파일:

```typescript
const formData = new FormData();

files.forEach((file) => {
  formData.append("images", file);
});
```

JSON 객체를 함께 보내는 경우:

```typescript
const request = {
  festivalId,
  rating,
  content,
};

const formData = new FormData();

formData.append(
  "request",
  new Blob([JSON.stringify(request)], {
    type: "application/json",
  }),
);

files.forEach((file) => {
  formData.append("images", file);
});
```

주의:

- Backend가 `request` part 이름을 기대하면 Frontend도 같은 이름 사용
- Backend가 `images`를 기대하면 `formData.append("images", file)` 사용
- field name 불일치 시 파일이나 DTO가 null로 들어갈 수 있음
- FormData 내용은 일반 객체처럼 console.log로 잘 안 보일 수 있음

---

### [FAQ]

Q. FormData에는 파일만 넣을 수 있어?
A. 아니다. 파일, 문자열, Blob, JSON 문자열 등을 함께 넣을 수 있다.

Q. FormData에 객체를 그대로 넣어도 돼?
A. 권장하지 않는다. 객체는 JSON.stringify 하거나 Blob으로 감싸서 보내는 것이 좋다.

Q. 여러 파일은 어떻게 넣어?
A. 같은 key로 여러 번 append할 수 있다. 예: `formData.append("images", file)` 반복.

Q. FormData key는 Frontend 마음대로 정해도 돼?
A. 아니다. Backend가 기대하는 multipart field name과 일치해야 한다.

---

# 4. multipart/form-data Rules

## 4.1 multipart 요청 기준

### [개념]

`multipart/form-data`는 파일과 텍스트 데이터를 함께 전송할 수 있는 HTTP Request 형식이다.

파일 업로드에서는 브라우저가 boundary를 포함한 Content-Type을 자동으로 구성하는 경우가 많다.

---

### [핵심]

multipart 핵심 키워드:

- multipart/form-data
- boundary
- FormData
- Content-Type
- Request Body
- MultipartFile
- @RequestPart
- @RequestParam
- file part
- JSON part

주의:

- multipart Content-Type을 수동으로 고정하지 않는 방식 권장
- boundary가 누락되면 Backend가 multipart를 파싱하지 못할 수 있음
- Axios와 fetch는 FormData 전달 시 boundary 처리 가능
- Backend field name과 FormData key 일치
- JSON API와 multipart API를 분리해서 이해

---

### [실무]

Axios multipart 요청:

```typescript
export async function uploadReviewImages(
  formData: FormData,
): Promise<ReviewImageResponse[]> {
  const response = await authApi.post<ApiResponse<ReviewImageResponse[]>>(
    "/reviews/images",
    formData,
  );

  return response.data.data;
}
```

fetch multipart 요청:

```typescript
export async function uploadImage(file: File) {
  const formData = new FormData();
  formData.append("image", file);

  const response = await fetch("/api/images", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to upload image");
  }

  return await response.json();
}
```

주의:

```typescript
// 권장하지 않는 예시
await authApi.post("/images", formData, {
  headers: {
    "Content-Type": "multipart/form-data",
  },
});
```

설명:

```text
FormData를 body로 전달하면 브라우저 / Axios가 boundary 포함 Content-Type을 처리할 수 있다.
Content-Type을 직접 고정하면 boundary 누락 문제가 생길 수 있다.
```

---

### [FAQ]

Q. multipart/form-data는 언제 써?
A. 파일 업로드처럼 파일과 텍스트 데이터를 함께 서버로 보낼 때 사용한다.

Q. Content-Type을 직접 multipart/form-data로 설정해야 해?
A. FormData를 사용할 때는 boundary 처리를 위해 직접 고정하지 않는 방식이 안전한 경우가 많다.

Q. boundary가 뭐야?
A. multipart 요청에서 각 part를 구분하기 위한 구분자다.

Q. JSON 요청과 multipart 요청은 달라?
A. 다르다. JSON 요청은 application/json body를 사용하고 multipart 요청은 FormData body를 사용한다.

---

# 5. Axios File Upload Rules

## 5.1 Axios 파일 업로드 기준

### [개념]

Axios File Upload는 FormData를 Axios POST / PATCH 요청의 body로 전달해 파일을 업로드하는 방식이다.

authApi를 사용하면 Authorization Header를 interceptor로 함께 처리할 수 있다.

---

### [핵심]

Axios File Upload 구성:

- authApi.post
- FormData
- file part
- request part
- response.data
- ApiResponse wrapper
- Authorization Header
- Upload Loading
- Error Handling
- onUploadProgress

주의:

- FormData를 두 번째 인자로 전달
- Header config는 세 번째 인자
- multipart Content-Type 수동 설정 주의
- authApi 사용 시 token 포함 여부 확인
- 업로드 실패 시 Error State 처리
- 응답 URL 또는 fileId mapping

---

### [실무]

단일 이미지 업로드:

```typescript
export type ImageUploadResponse = {
  imageId: number;
  imageUrl: string;
};

export async function uploadImage(file: File): Promise<ImageUploadResponse> {
  const formData = new FormData();
  formData.append("image", file);

  const response = await authApi.post<ApiResponse<ImageUploadResponse>>(
    "/images",
    formData,
  );

  return response.data.data;
}
```

여러 이미지 업로드:

```typescript
export async function uploadImages(
  files: File[],
): Promise<ImageUploadResponse[]> {
  const formData = new FormData();

  files.forEach((file) => {
    formData.append("images", file);
  });

  const response = await authApi.post<ApiResponse<ImageUploadResponse[]>>(
    "/images/bulk",
    formData,
  );

  return response.data.data;
}
```

업로드 진행률:

```typescript
export async function uploadImageWithProgress(
  file: File,
  onProgress: (progress: number) => void,
): Promise<ImageUploadResponse> {
  const formData = new FormData();
  formData.append("image", file);

  const response = await authApi.post<ApiResponse<ImageUploadResponse>>(
    "/images",
    formData,
    {
      onUploadProgress: (event) => {
        if (!event.total) {
          return;
        }

        const progress = Math.round((event.loaded * 100) / event.total);
        onProgress(progress);
      },
    },
  );

  return response.data.data;
}
```

---

### [FAQ]

Q. Axios에서 파일은 어디에 넣어?
A. FormData를 만들고 `authApi.post(url, formData)`의 두 번째 인자로 넣는다.

Q. 업로드 진행률은 어떻게 얻어?
A. Axios의 `onUploadProgress` 옵션을 사용할 수 있다.

Q. 파일 업로드도 authApi를 써?
A. 인증이 필요한 업로드라면 authApi를 사용해 Authorization Header를 포함한다.

Q. 여러 파일은 어떻게 업로드해?
A. FormData에 같은 key로 여러 File을 append하고 Backend가 해당 key를 배열로 받도록 맞춘다.

---

# 6. fetch File Upload Rules

## 6.1 fetch 파일 업로드 기준

### [개념]

fetch File Upload는 FormData를 fetch 요청의 body로 전달하는 방식이다.

fetch는 HTTP Error를 자동 throw하지 않으므로 `response.ok`를 직접 확인해야 한다.

---

### [핵심]

fetch File Upload 구성:

- fetch
- method POST
- FormData
- body
- Authorization Header
- response.ok
- response.json
- Error Handling

주의:

- FormData 사용 시 Content-Type 직접 설정 주의
- Authorization Header는 직접 추가
- fetch는 400 / 500을 자동 throw하지 않음
- response.ok 확인 필요
- 204 No Content 응답 처리 필요
- 업로드 진행률은 fetch에서 기본 구현이 제한적

---

### [실무]

fetch 단일 업로드:

```typescript
export async function uploadImage(file: File) {
  const formData = new FormData();
  formData.append("image", file);

  const response = await fetch("/api/images", {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Upload failed: ${response.status}`);
  }

  return await response.json();
}
```

Authorization Header 포함:

```typescript
export async function uploadImage(file: File, accessToken: string) {
  const formData = new FormData();
  formData.append("image", file);

  const response = await fetch("/api/images", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${accessToken}`,
    },
    body: formData,
  });

  if (!response.ok) {
    throw new Error(`Upload failed: ${response.status}`);
  }

  return await response.json();
}
```

주의:

```typescript
// FormData 요청에서 직접 Content-Type을 고정하지 않음
headers: {
  Authorization: `Bearer ${accessToken}`,
}
```

---

### [FAQ]

Q. fetch로도 파일 업로드가 가능해?
A. 가능하다. FormData를 body로 넣어 POST 요청을 보내면 된다.

Q. fetch 파일 업로드에서도 response.ok를 확인해야 해?
A. 해야 한다. fetch는 HTTP Error를 자동으로 throw하지 않는다.

Q. fetch에서 업로드 진행률을 쉽게 볼 수 있어?
A. 기본 fetch만으로는 제한적이다. 진행률이 중요하면 Axios나 별도 구현을 검토한다.

Q. fetch multipart 요청에서 Content-Type을 직접 설정해야 해?
A. FormData를 사용할 때는 boundary 처리를 위해 직접 설정하지 않는 것이 안전한 경우가 많다.

---

# 7. File Validation Rules

## 7.1 파일 검증 기준

### [개념]

File Validation은 업로드 전 파일 크기, 파일 타입, 확장자, 개수 등을 확인하는 과정이다.

Frontend 검증은 사용자 경험을 개선하지만 보안의 최종 기준은 Backend 검증이다.

---

### [핵심]

검증 대상:

- file size
- file type
- file extension
- file count
- image only
- video only
- pdf only
- empty file
- duplicate file
- filename length

주의:

- accept 속성만 믿지 않음
- file.type이 비어 있을 수 있음
- 확장자만 믿지 않음
- Backend 검증 필수
- 에러 메시지는 사용자 친화적으로 제공
- 대용량 파일은 업로드 전 차단

---

### [실무]

파일 크기 검증:

```typescript
const MAX_FILE_SIZE = 5 * 1024 * 1024;

export function validateFileSize(file: File): string {
  if (file.size > MAX_FILE_SIZE) {
    return "파일 크기는 5MB 이하만 업로드할 수 있습니다.";
  }

  return "";
}
```

이미지 타입 검증:

```typescript
const ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];

export function validateImageType(file: File): string {
  if (!ALLOWED_IMAGE_TYPES.includes(file.type)) {
    return "jpg, png, webp 이미지만 업로드할 수 있습니다.";
  }

  return "";
}
```

여러 파일 검증:

```typescript
const MAX_FILE_COUNT = 5;

export function validateFiles(files: File[]): string {
  if (files.length > MAX_FILE_COUNT) {
    return "최대 5개까지 업로드할 수 있습니다.";
  }

  for (const file of files) {
    const sizeError = validateFileSize(file);
    const typeError = validateImageType(file);

    if (sizeError) {
      return sizeError;
    }

    if (typeError) {
      return typeError;
    }
  }

  return "";
}
```

---

### [FAQ]

Q. 파일 검증은 Frontend에서만 하면 돼?
A. 아니다. Frontend 검증은 UX용이고 Backend에서 반드시 최종 검증해야 한다.

Q. accept 속성이 있으면 파일 타입 검증이 필요 없어?
A. 필요하다. accept는 선택 창의 힌트일 뿐 완전한 보안 검증이 아니다.

Q. file.type만 믿어도 돼?
A. 완전히 신뢰하면 안 된다. Backend에서 MIME type, 확장자, 파일 내용 검증이 필요하다.

Q. 파일 크기 제한은 왜 필요해?
A. 네트워크 비용, 서버 저장소, 사용자 대기 시간, 보안 문제를 줄이기 위해 필요하다.

---

# 8. Image Preview Rules

## 8.1 이미지 미리보기 기준

### [개념]

Image Preview는 사용자가 선택한 이미지를 업로드 전에 화면에서 확인할 수 있게 하는 UX 기능이다.

브라우저에서는 `URL.createObjectURL(file)`을 사용해 임시 preview URL을 만들 수 있다.

---

### [핵심]

Preview 핵심 키워드:

- URL.createObjectURL
- URL.revokeObjectURL
- previewUrl
- File object
- image preview
- cleanup
- memory leak
- selected file

주의:

- createObjectURL 사용 후 revokeObjectURL 필요
- 파일 변경 시 이전 preview URL 정리
- Component unmount 시 cleanup
- preview는 업로드 완료 URL이 아님
- preview URL은 브라우저 임시 URL
- 업로드 성공 후 Backend imageUrl로 교체 가능

---

### [실무]

단일 이미지 Preview:

```tsx
function ImagePreviewInput() {
  const [file, setFile] = useState<File | null>(null);
  const [previewUrl, setPreviewUrl] = useState("");

  useEffect(() => {
    if (!file) {
      setPreviewUrl("");
      return;
    }

    const objectUrl = URL.createObjectURL(file);
    setPreviewUrl(objectUrl);

    return () => {
      URL.revokeObjectURL(objectUrl);
    };
  }, [file]);

  function handleChange(event: React.ChangeEvent<HTMLInputElement>) {
    const selectedFile = event.target.files?.[0] ?? null;
    setFile(selectedFile);
  }

  return (
    <>
      <input type="file" accept="image/*" onChange={handleChange} />
      {previewUrl && <img src={previewUrl} alt="선택한 이미지 미리보기" />}
    </>
  );
}
```

여러 이미지 Preview:

```tsx
function createPreviewItems(files: File[]) {
  return files.map((file) => ({
    file,
    previewUrl: URL.createObjectURL(file),
  }));
}
```

cleanup 기준:

```typescript
previewItems.forEach((item) => {
  URL.revokeObjectURL(item.previewUrl);
});
```

---

### [FAQ]

Q. 이미지 미리보기는 어떻게 만들어?
A. `URL.createObjectURL(file)`로 임시 preview URL을 만들 수 있다.

Q. revokeObjectURL은 왜 필요해?
A. 임시 URL을 정리하지 않으면 메모리 누수가 발생할 수 있기 때문이다.

Q. previewUrl은 서버 이미지 URL이야?
A. 아니다. 브라우저에서 만든 임시 URL이다. 업로드 성공 후 서버 imageUrl을 따로 받아야 한다.

Q. 파일을 바꾸면 이전 preview는 어떻게 해?
A. 이전 preview URL을 revoke하고 새 파일의 preview URL을 만든다.

---

# 9. Upload UI State Rules

## 9.1 업로드 상태 처리 기준

### [개념]

Upload UI State는 파일 업로드 과정의 Loading, Error, Progress, Success 상태를 관리하는 기준이다.

파일 업로드는 일반 API 요청보다 시간이 오래 걸릴 수 있으므로 사용자에게 진행 상태를 명확히 알려야 한다.

---

### [핵심]

Upload State 요소:

- selectedFile
- selectedFiles
- uploading
- uploadProgress
- uploadError
- uploadedFileUrl
- uploadedFileId
- previewUrl
- validationError

상태 구분:

```text
No File Selected
→ File Selected
→ Validation Error or Ready
→ Uploading
→ Upload Success or Upload Error
```

주의:

- 업로드 중 버튼 disabled
- 업로드 실패 시 선택 파일 유지 가능
- 성공 후 file id / URL 저장
- progress는 optional
- validation error와 upload error 구분
- 업로드 중 파일 변경 제한 여부 결정

---

### [실무]

Upload State:

```typescript
type UploadState = {
  file: File | null;
  uploading: boolean;
  progress: number;
  errorMessage: string;
  uploadedUrl: string;
};
```

업로드 함수:

```tsx
async function handleUpload() {
  if (!file) {
    setErrorMessage("업로드할 파일을 선택해 주세요.");
    return;
  }

  const validationError = validateImageType(file) || validateFileSize(file);

  if (validationError) {
    setErrorMessage(validationError);
    return;
  }

  try {
    setUploading(true);
    setErrorMessage("");

    const uploaded = await uploadImageWithProgress(file, setProgress);
    setUploadedUrl(uploaded.imageUrl);
  } catch (error) {
    setErrorMessage(getApiErrorMessage(error));
  } finally {
    setUploading(false);
  }
}
```

UI:

```tsx
<button type="button" disabled={!file || uploading} onClick={handleUpload}>
  {uploading ? "업로드 중..." : "업로드"}
</button>;

{
  uploading && <progress value={progress} max={100} />;
}

{
  errorMessage && <p role="alert">{errorMessage}</p>;
}
```

---

### [FAQ]

Q. 파일 업로드 중 버튼을 disabled 해야 해?
A. 중복 업로드를 막기 위해 업로드 중에는 버튼을 disabled 처리하는 것이 좋다.

Q. 업로드 실패 시 선택한 파일은 지워야 해?
A. 보통 유지하는 것이 좋다. 사용자가 다시 시도할 수 있어야 한다.

Q. validation error와 upload error는 달라?
A. 다르다. validation error는 요청 전 파일 검증 실패이고 upload error는 서버 요청 실패다.

Q. 업로드 진행률은 꼭 보여줘야 해?
A. 파일이 작으면 필수는 아니지만 대용량 파일이나 느린 네트워크에서는 유용하다.

---

# 10. File Upload with Form Rules

## 10.1 Form 제출과 파일 업로드 조합

### [개념]

File Upload with Form은 텍스트 입력값과 파일을 함께 제출하는 방식이다.

Backend API 설계에 따라 하나의 multipart request로 보내거나, 파일을 먼저 업로드한 뒤 반환된 fileId / imageUrl을 JSON Request에 포함할 수 있다.

---

### [핵심]

전략 1:

```text
FormData에 JSON Part + File Part 함께 전송
```

전략 2:

```text
File Upload API 먼저 호출
→ imageUrl or fileId 응답
→ JSON Create API 호출
```

선택 기준:

- Backend API 명세
- 파일 업로드 실패 처리
- Form Validation 복잡도
- 재사용성
- 트랜잭션 요구사항
- 이미지 재사용 여부

주의:

- JSON API와 File API 책임 구분
- 파일 업로드 성공 후 게시글 작성 실패 시 orphan file 처리 고려
- 하나의 multipart 요청이면 Backend `@RequestPart` 기준 확인
- 두 단계 요청이면 중간 실패 상태 처리 필요

---

### [실무]

전략 1: multipart로 한 번에 제출

```typescript
export async function createReviewWithImages(
  request: ReviewCreateRequest,
  files: File[],
): Promise<ReviewResponse> {
  const formData = new FormData();

  formData.append(
    "request",
    new Blob([JSON.stringify(request)], {
      type: "application/json",
    }),
  );

  files.forEach((file) => {
    formData.append("images", file);
  });

  const response = await authApi.post<ApiResponse<ReviewResponse>>(
    "/reviews",
    formData,
  );

  return response.data.data;
}
```

전략 2: 파일 먼저 업로드 후 JSON 제출

```typescript
async function submitReview() {
  const uploadedImages = await uploadImages(files);

  const requestBody: ReviewCreateRequest = {
    festivalId,
    rating,
    content,
    imageUrls: uploadedImages.map((image) => image.imageUrl),
  };

  await createReview(requestBody);
}
```

주의:

- Backend가 어떤 전략을 요구하는지 우선 확인
- 한 번에 전송하면 요청 구성은 복잡하지만 흐름은 단순
- 두 단계 전송은 API 재사용성이 좋지만 실패 보상 처리 고려
- UI에서는 전체 submit loading으로 관리

---

### [FAQ]

Q. 파일과 글 내용을 한 번에 보낼 수 있어?
A. 가능하다. FormData에 JSON part와 file part를 함께 넣어 multipart 요청으로 보낼 수 있다.

Q. 파일을 먼저 업로드하고 URL만 저장하는 방식도 가능해?
A. 가능하다. 파일 업로드 API가 imageUrl이나 fileId를 반환하면 이후 JSON 요청에 포함할 수 있다.

Q. 어떤 방식이 더 좋아?
A. Backend API 설계와 트랜잭션 요구사항에 따라 다르다.

Q. 파일 업로드 성공 후 글 작성 실패하면 어떻게 해?
A. orphan file이 생길 수 있으므로 Backend 정리 정책이나 실패 보상 처리를 고려해야 한다.

---

# 11. Multiple File Upload Rules

## 11.1 다중 파일 업로드 기준

### [개념]

Multiple File Upload는 여러 File 객체를 하나의 요청 또는 여러 요청으로 Backend에 전송하는 방식이다.

이미지 갤러리, 리뷰 이미지, 게시글 첨부파일 등에 사용한다.

---

### [핵심]

다중 파일 처리 기준:

- multiple input
- File[]
- FormData append 반복
- max file count
- total size limit
- per file validation
- preview list
- remove selected file
- order
- upload progress

주의:

- 파일 개수 제한
- 파일별 크기 제한
- 전체 용량 제한
- 중복 파일 처리
- 파일 순서 필요 여부 확인
- 실패 시 전체 실패 / 부분 성공 정책 확인
- Backend field name과 일치

---

### [실무]

여러 파일 선택:

```tsx
function handleFileChange(event: React.ChangeEvent<HTMLInputElement>) {
  const selectedFiles = Array.from(event.target.files ?? []);

  const validationError = validateFiles(selectedFiles);

  if (validationError) {
    setErrorMessage(validationError);
    return;
  }

  setFiles(selectedFiles);
}
```

선택 파일 제거:

```typescript
function removeFile(index: number) {
  setFiles((prev) => prev.filter((_, currentIndex) => currentIndex !== index));
}
```

다중 파일 FormData:

```typescript
const formData = new FormData();

files.forEach((file) => {
  formData.append("images", file);
});
```

다중 업로드 API:

```typescript
export async function uploadReviewImages(
  files: File[],
): Promise<ImageUploadResponse[]> {
  const formData = new FormData();

  files.forEach((file) => {
    formData.append("images", file);
  });

  const response = await authApi.post<ApiResponse<ImageUploadResponse[]>>(
    "/reviews/images",
    formData,
  );

  return response.data.data;
}
```

---

### [FAQ]

Q. 여러 파일은 FormData에 어떻게 넣어?
A. 같은 key로 여러 번 append한다. 예: `formData.append("images", file)` 반복.

Q. 파일 개수 제한은 Frontend에서 해야 해?
A. UX를 위해 Frontend에서 먼저 하고, Backend에서도 반드시 검증해야 한다.

Q. 선택한 파일 하나만 제거할 수 있어?
A. 가능하다. File 배열 상태에서 해당 index를 제거하면 된다.

Q. 다중 파일 업로드에서 일부만 실패하면 어떻게 해?
A. Backend API 정책에 따라 전체 실패 또는 부분 성공으로 처리할 수 있으므로 응답 구조를 확인해야 한다.

---

# 12. Upload Response Mapping Rules

## 12.1 업로드 응답 DTO 처리 기준

### [개념]

Upload Response Mapping은 파일 업로드 성공 후 Backend가 반환한 fileId, imageUrl, originalName, storedName, size 같은 정보를 Frontend 상태와 UI에 반영하는 작업이다.

---

### [핵심]

Upload Response 필드 예:

- fileId
- imageId
- imageUrl
- originalFileName
- storedFileName
- contentType
- size
- sortOrder
- uploadedAt

처리 기준:

- imageUrl을 preview 대신 실제 표시 URL로 사용
- fileId를 이후 JSON Request에 포함 가능
- originalFileName은 사용자 표시용
- storedFileName은 내부 값일 수 있음
- 응답 DTO와 UI ViewModel 구분
- 다중 업로드 응답은 배열로 처리

주의:

- previewUrl과 imageUrl 구분
- Backend 상대 경로 / 절대 경로 확인
- imageUrl이 null 가능하면 fallback 처리
- 파일 삭제 API가 있으면 fileId 저장 필요
- 응답 구조는 Network Response 기준 확인

---

### [실무]

Upload Response Type:

```typescript
export type ImageUploadResponse = {
  imageId: number;
  imageUrl: string;
  originalFileName: string;
  size: number;
  contentType: string;
};
```

업로드 후 상태 반영:

```typescript
const uploaded = await uploadImage(file);

setUploadedImage({
  imageId: uploaded.imageId,
  imageUrl: uploaded.imageUrl,
  originalFileName: uploaded.originalFileName,
});
```

다중 업로드 후 JSON 요청 연결:

```typescript
const uploadedImages = await uploadReviewImages(files);

const requestBody = {
  festivalId,
  rating,
  content,
  imageIds: uploadedImages.map((image) => image.imageId),
};

await createReview(requestBody);
```

주의:

- Backend가 imageUrl이 아니라 imageId만 반환할 수 있음
- 반환값에 맞춰 후속 API Request DTO 설계
- imageUrl은 사용자 표시용, imageId는 서버 연계용일 수 있음
- 업로드 성공 후 미리보기 URL cleanup 가능

---

### [FAQ]

Q. 업로드 성공 후 뭘 저장해야 해?
A. Backend 응답에 따라 imageUrl, imageId, originalFileName 등을 상태에 저장한다.

Q. previewUrl과 imageUrl은 달라?
A. 다르다. previewUrl은 브라우저 임시 URL이고 imageUrl은 서버에 저장된 파일 접근 URL이다.

Q. 후속 요청에는 imageUrl을 보내야 해 imageId를 보내야 해?
A. Backend API 명세에 따라 다르다. 서버가 fileId를 기대하면 imageId를 보내야 한다.

Q. 업로드 응답 구조는 어디서 확인해?
A. Network 탭의 Response Body와 Backend API 명세를 확인한다.

---

# 13. File Delete and Replace Rules

## 13.1 파일 삭제 / 교체 기준

### [개념]

File Delete and Replace는 이미 업로드된 파일을 삭제하거나 새 파일로 교체하는 API 흐름이다.

프로필 이미지 변경, 리뷰 이미지 삭제, 게시글 첨부파일 수정에서 사용한다.

---

### [핵심]

삭제 / 교체 상황:

- selected file 제거
- uploaded file 삭제
- profile image replace
- review image delete
- attachment delete
- image order change

처리 기준:

- 아직 업로드 전 파일 제거는 Frontend state에서만 처리
- 이미 업로드된 파일 삭제는 Backend Delete API 필요
- 교체는 upload new file + delete old file 또는 replace API 사용
- 삭제 성공 후 UI 상태 갱신
- 실패 시 기존 파일 상태 유지
- 권한 확인 필요

주의:

- 로컬 preview 제거와 서버 파일 삭제를 구분
- fileId / imageId 필요
- 삭제 API 실패 시 UI에서 바로 제거하면 불일치 가능
- Optimistic update 사용 시 rollback 필요
- Backend 저장소 정리 정책 확인

---

### [실무]

업로드 전 선택 파일 제거:

```typescript
function removeSelectedFile(index: number) {
  setFiles((prev) => prev.filter((_, currentIndex) => currentIndex !== index));
}
```

업로드된 이미지 삭제 API:

```typescript
export async function deleteImage(imageId: number): Promise<void> {
  await authApi.delete(`/images/${imageId}`);
}
```

삭제 후 UI 갱신:

```typescript
async function handleDeleteImage(imageId: number) {
  try {
    await deleteImage(imageId);

    setUploadedImages((prev) =>
      prev.filter((image) => image.imageId !== imageId),
    );
  } catch (error) {
    setErrorMessage(getApiErrorMessage(error));
  }
}
```

교체 Flow:

```text
User Select New File
→ Validate New File
→ Upload New File or Replace API
→ Response New imageUrl
→ Update UI
→ Delete Old File if required
```

---

### [FAQ]

Q. 업로드 전 선택한 파일 삭제는 API가 필요해?
A. 아니다. 아직 서버에 업로드하지 않았다면 Frontend state에서만 제거하면 된다.

Q. 이미 업로드된 파일 삭제는 API가 필요해?
A. 필요하다. 서버 저장소에서 삭제하려면 Backend Delete API를 호출해야 한다.

Q. 파일 교체는 어떻게 해?
A. 새 파일 업로드 후 기존 파일 삭제 또는 Backend replace API를 사용할 수 있다.

Q. 삭제 실패 시 UI에서 파일을 지워도 돼?
A. 권장하지 않는다. 서버 삭제 실패 시 UI와 서버 상태가 불일치할 수 있다.

---

# 14. Security Rules

## 14.1 File Upload 보안 기준

### [개념]

File Upload는 보안 위험이 큰 기능이다.

Frontend 검증은 UX용이며 파일 크기, 확장자, MIME type, 파일 내용, 저장 경로, 접근 권한 검증은 Backend에서 최종 처리해야 한다.

---

### [핵심]

보안 검증 대상:

- file size
- file extension
- MIME type
- file content
- executable file
- script file
- path traversal
- filename sanitization
- access control
- virus scanning
- storage permission
- public URL exposure

Frontend 기준:

- 허용 파일 타입 안내
- 허용 크기 제한 안내
- 업로드 전 UX 검증
- 민감 파일 업로드 주의 문구
- token 로그 금지
- file metadata 노출 주의

Backend 최종 기준:

- 파일 타입 검증
- 저장 파일명 재생성
- 경로 조작 방지
- 권한 확인
- 공개 / 비공개 접근 제어
- 악성 파일 차단
- 저장소 정책 적용

---

### [실무]

Frontend 검증:

```typescript
const ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/webp"];
const MAX_IMAGE_SIZE = 5 * 1024 * 1024;
```

금지 파일 UX 안내:

```text
jpg, png, webp 이미지 파일만 업로드할 수 있습니다.
파일 크기는 5MB 이하만 가능합니다.
```

주의:

- Frontend에서 확장자를 제한해도 공격자가 우회 가능
- 파일명은 서버에서 신뢰하지 않음
- 사용자가 업로드한 파일을 그대로 실행 가능한 경로에 두지 않음
- 공개 URL이 필요한 파일과 인증 후 접근 파일 구분
- Authorization Header와 파일 metadata 로그 노출 주의

---

### [FAQ]

Q. File Upload는 보안상 위험해?
A. 위험할 수 있다. 악성 파일, 경로 조작, 용량 공격, 권한 문제를 Backend에서 반드시 검증해야 한다.

Q. Frontend 파일 검증만으로 충분해?
A. 아니다. Frontend 검증은 우회 가능하므로 Backend 검증이 최종 기준이다.

Q. 파일명은 그대로 저장해도 돼?
A. 권장하지 않는다. 서버에서 안전한 저장 파일명으로 재생성하는 것이 좋다.

Q. 업로드 파일 URL은 모두 공개해도 돼?
A. 파일 성격에 따라 다르다. 민감 파일은 인증과 권한 검사를 거쳐 접근해야 한다.

---

# 15. File Upload Testing and Debugging Rules

## 15.1 파일 업로드 검수 기준

### [개념]

File Upload Testing은 파일 선택, 검증, FormData 구성, multipart 요청, Backend 응답, UI 상태 갱신이 정상 동작하는지 확인하는 과정이다.

---

### [핵심]

검수 대상:

- file input
- selected file
- file size validation
- file type validation
- FormData key
- multipart request
- Request Headers
- Authorization Header
- Request Payload
- Response Body
- imageUrl mapping
- upload loading
- upload error
- duplicate upload
- preview cleanup

검수 도구:

- Browser Network Tab
- Request Payload
- Backend API Spec
- Swagger UI
- Postman
- Console Debug
- Storage Console
- Backend Log

---

### [실무]

Debug Flow:

```text
Upload Failed
→ selected file 확인
→ validation 통과 확인
→ FormData key 확인
→ Network Request Payload 확인
→ Authorization Header 확인
→ Content-Type boundary 확인
→ Backend field name 확인
→ Response Body 확인
→ UI Error State 확인
```

FormData 확인:

```typescript
for (const [key, value] of formData.entries()) {
  console.log(key, value);
}
```

Network 확인:

```text
Network Tab
→ Request Method POST
→ Request Headers
→ Authorization Header
→ Content-Type multipart/form-data; boundary=...
→ Payload Form Data
→ Response Body
```

상황별 문제:

```text
파일이 Backend에서 null
→ FormData key와 Backend @RequestPart name 확인
```

```text
415 Unsupported Media Type
→ multipart 요청 형식 / Content-Type 설정 확인
```

```text
401 Unauthorized
→ authApi 사용 여부 / Authorization Header 확인
```

```text
업로드 성공인데 이미지 안 보임
→ response imageUrl / 정적 파일 접근 URL / CORS / storage 권한 확인
```

---

### [FAQ]

Q. 파일 업로드가 실패하면 뭘 먼저 봐?
A. Network 탭에서 Request Payload, Content-Type, Authorization Header, Response Body를 확인한다.

Q. Backend에서 파일이 null로 들어가?
A. FormData key와 Backend가 기대하는 multipart field name이 일치하는지 확인해야 한다.

Q. 415 Unsupported Media Type은 왜 나?
A. Content-Type이나 multipart 요청 형식이 Backend가 기대하는 형식과 다를 때 발생할 수 있다.

Q. 업로드 성공했는데 이미지가 안 보여?
A. 응답 imageUrl, 정적 파일 접근 경로, storage 권한, CORS, 이미지 URL 유효성을 확인한다.

---

# 16. Common Mistakes

## 16.1 File Upload 공통 실수

### [개념]

File Upload 실수는 JSON 요청과 multipart 요청을 혼동하거나, FormData key, Content-Type, 파일 검증, 업로드 상태 처리를 놓칠 때 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 파일을 JSON body로 보내려고 함
- FormData를 사용하지 않음
- FormData key와 Backend field name 불일치
- 여러 파일 append key 불일치
- 객체를 FormData에 그대로 append
- multipart Content-Type을 수동 고정해 boundary 누락
- file input accept만 믿고 검증 생략
- Backend 파일 검증 생략
- 파일 크기 제한 없음
- 업로드 중 버튼 disabled 없음
- 중복 업로드 발생
- 업로드 실패 시 loading 종료 누락
- preview URL revoke 누락
- previewUrl과 imageUrl 혼동
- 업로드 성공 후 응답 DTO mapping 누락
- 업로드된 파일 삭제와 선택 파일 제거 혼동
- authApi 대신 publicApi로 업로드
- Authorization Header 누락
- 415 오류를 CORS 오류로 착각
- Backend에서 파일 null인데 Network Payload 미확인

---

### [실무]

문제 예:

```text
문제: Backend MultipartFile이 null
원인: FormData key가 Backend @RequestPart name과 다름
해결: formData.append("image", file)와 Backend part name 일치
```

문제 예:

```text
문제: 415 Unsupported Media Type
원인: multipart 요청 Content-Type 설정 오류
해결: FormData 전달 시 Content-Type 직접 고정 제거 검토
```

문제 예:

```text
문제: 업로드 후 미리보기 메모리 누수
원인: createObjectURL 후 revokeObjectURL 누락
해결: useEffect cleanup에서 URL.revokeObjectURL 호출
```

문제 예:

```text
문제: 업로드 성공 후 이미지가 안 보임
원인: previewUrl과 서버 imageUrl을 혼동하거나 imageUrl mapping 누락
해결: Upload Response의 imageUrl을 UI 상태에 저장
```

해결 우선순위:

```text
File 선택 확인
→ File Validation 확인
→ FormData key 확인
→ Network Payload 확인
→ Content-Type boundary 확인
→ Authorization Header 확인
→ Backend field name 확인
→ Response DTO 확인
→ UI Mapping 확인
```

---

### [FAQ]

Q. File Upload에서 가장 흔한 실수는?
A. FormData key와 Backend multipart field name을 맞추지 않거나 Content-Type boundary를 깨뜨리는 것이다.

Q. 파일을 JSON body로 보내면 안 돼?
A. 일반 파일 업로드는 JSON body가 아니라 multipart FormData로 보내는 것이 일반적이다.

Q. previewUrl을 DB에 저장해도 돼?
A. 안 된다. previewUrl은 브라우저 임시 URL이므로 서버에서 반환한 imageUrl이나 fileId를 저장해야 한다.

Q. 업로드 API가 401이면 뭘 봐?
A. authApi 사용 여부와 Authorization Header 포함 여부를 Network 탭에서 확인해야 한다.

---

# 17. Part09 Checklist

## 17.1 File Upload 검수 기준

### [개념]

Part09 File Upload 문서는 Frontend Agent가 FormData, multipart/form-data, 파일 검증, 이미지 미리보기, 업로드 상태, 응답 mapping, 보안 기준을 적용해 파일 업로드 API를 안정적으로 구현하도록 만드는 문서다.

---

### [핵심]

Checklist:

```md
- [ ] File Upload 기본 개념이 포함되었는가?
- [ ] File Input 기준이 포함되었는가?
- [ ] FormData 기준이 포함되었는가?
- [ ] multipart/form-data 기준이 포함되었는가?
- [ ] Axios File Upload 기준이 포함되었는가?
- [ ] fetch File Upload 기준이 포함되었는가?
- [ ] File Validation 기준이 포함되었는가?
- [ ] Image Preview 기준이 포함되었는가?
- [ ] Upload UI State 기준이 포함되었는가?
- [ ] Form 제출과 파일 업로드 조합 기준이 포함되었는가?
- [ ] Multiple File Upload 기준이 포함되었는가?
- [ ] Upload Response Mapping 기준이 포함되었는가?
- [ ] File Delete and Replace 기준이 포함되었는가?
- [ ] Security 기준이 포함되었는가?
- [ ] File Upload Testing and Debugging 기준이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ File Input Check
→ FormData Check
→ multipart Request Check
→ Axios / fetch Upload Check
→ File Validation Check
→ Preview Cleanup Check
→ Upload State Check
→ Response Mapping Check
→ Delete / Replace Check
→ Security Check
→ Network Debugging Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

최종 기준:

- File Input에서 File 객체 획득 가능
- FormData로 multipart 요청 구성 가능
- Backend multipart field name과 FormData key 일치 가능
- Axios / fetch 파일 업로드 코드 생성 가능
- 파일 크기 / 타입 / 개수 검증 가능
- 이미지 preview와 cleanup 처리 가능
- Upload Loading / Error / Progress UI 처리 가능
- 업로드 응답 DTO를 UI와 후속 요청에 mapping 가능
- File Upload 보안 기준을 Frontend / Backend로 구분 가능
- Frontend Agent가 안정적인 File Upload API 연동 코드를 생성 가능

---

### [FAQ]

Q. Part09의 목적은 뭐야?
A. Frontend Agent가 FormData와 multipart/form-data를 사용해 파일 업로드 API를 안정적으로 구현하게 만드는 것이다.

Q. Part09에서 가장 중요한 기준은 뭐야?
A. FormData key와 Backend field name 일치, multipart Content-Type boundary 처리, 파일 검증, 업로드 상태 처리다.

Q. Part09 다음에는 어떤 문서가 이어지면 좋아?
A. API Troubleshooting, CORS / 401 / 403 / 404 Debugging, API Testing, Authentication Frontend Flow 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. File Upload는 JSON으로 보내?
A. 일반적으로 파일은 JSON이 아니라 FormData와 multipart/form-data로 보낸다.

Q. FormData는 뭐야?
A. 파일과 텍스트 필드를 함께 전송할 수 있는 브라우저 API다.

Q. File Upload에서도 Axios를 쓸 수 있어?
A. 가능하다. Axios POST 요청의 body에 FormData를 넣어 전송할 수 있다.

Q. File Upload에서 가장 중요한 주의점은 뭐야?
A. FormData 사용, 파일 검증, 업로드 상태 처리, multipart Content-Type boundary 처리 기준이다.

Q. File 객체는 어디서 얻어?
A. `input[type="file"]`의 `event.target.files`에서 얻는다.

Q. 단일 파일은 어떻게 가져와?
A. `event.target.files?.[0]`로 가져올 수 있다.

Q. multiple 속성은 언제 써?
A. 여러 파일을 한 번에 선택해야 할 때 사용한다.

Q. accept="image/\*"면 이미지 파일만 완전히 막을 수 있어?
A. 아니다. accept는 사용자 선택을 돕는 힌트이고 실제 검증은 Frontend와 Backend에서 따로 해야 한다.

Q. FormData에는 파일만 넣을 수 있어?
A. 아니다. 파일, 문자열, Blob, JSON 문자열 등을 함께 넣을 수 있다.

Q. FormData에 객체를 그대로 넣어도 돼?
A. 권장하지 않는다. 객체는 JSON.stringify 하거나 Blob으로 감싸서 보내는 것이 좋다.

Q. 여러 파일은 어떻게 넣어?
A. 같은 key로 여러 번 append할 수 있다. 예: `formData.append("images", file)` 반복.

Q. FormData key는 Frontend 마음대로 정해도 돼?
A. 아니다. Backend가 기대하는 multipart field name과 일치해야 한다.

Q. multipart/form-data는 언제 써?
A. 파일 업로드처럼 파일과 텍스트 데이터를 함께 서버로 보낼 때 사용한다.

Q. Content-Type을 직접 multipart/form-data로 설정해야 해?
A. FormData를 사용할 때는 boundary 처리를 위해 직접 고정하지 않는 방식이 안전한 경우가 많다.

Q. boundary가 뭐야?
A. multipart 요청에서 각 part를 구분하기 위한 구분자다.

Q. JSON 요청과 multipart 요청은 달라?
A. 다르다. JSON 요청은 application/json body를 사용하고 multipart 요청은 FormData body를 사용한다.

Q. Axios에서 파일은 어디에 넣어?
A. FormData를 만들고 `authApi.post(url, formData)`의 두 번째 인자로 넣는다.

Q. 업로드 진행률은 어떻게 얻어?
A. Axios의 `onUploadProgress` 옵션을 사용할 수 있다.

Q. 파일 업로드도 authApi를 써?
A. 인증이 필요한 업로드라면 authApi를 사용해 Authorization Header를 포함한다.

Q. 여러 파일은 어떻게 업로드해?
A. FormData에 같은 key로 여러 File을 append하고 Backend가 해당 key를 배열로 받도록 맞춘다.

Q. fetch로도 파일 업로드가 가능해?
A. 가능하다. FormData를 body로 넣어 POST 요청을 보내면 된다.

Q. fetch 파일 업로드에서도 response.ok를 확인해야 해?
A. 해야 한다. fetch는 HTTP Error를 자동으로 throw하지 않는다.

Q. fetch에서 업로드 진행률을 쉽게 볼 수 있어?
A. 기본 fetch만으로는 제한적이다. 진행률이 중요하면 Axios나 별도 구현을 검토한다.

Q. fetch multipart 요청에서 Content-Type을 직접 설정해야 해?
A. FormData를 사용할 때는 boundary 처리를 위해 직접 설정하지 않는 것이 안전한 경우가 많다.

Q. 파일 검증은 Frontend에서만 하면 돼?
A. 아니다. Frontend 검증은 UX용이고 Backend에서 반드시 최종 검증해야 한다.

Q. accept 속성이 있으면 파일 타입 검증이 필요 없어?
A. 필요하다. accept는 선택 창의 힌트일 뿐 완전한 보안 검증이 아니다.

Q. file.type만 믿어도 돼?
A. 완전히 신뢰하면 안 된다. Backend에서 MIME type, 확장자, 파일 내용 검증이 필요하다.

Q. 파일 크기 제한은 왜 필요해?
A. 네트워크 비용, 서버 저장소, 사용자 대기 시간, 보안 문제를 줄이기 위해 필요하다.

Q. 이미지 미리보기는 어떻게 만들어?
A. `URL.createObjectURL(file)`로 임시 preview URL을 만들 수 있다.

Q. revokeObjectURL은 왜 필요해?
A. 임시 URL을 정리하지 않으면 메모리 누수가 발생할 수 있기 때문이다.

Q. previewUrl은 서버 이미지 URL이야?
A. 아니다. 브라우저에서 만든 임시 URL이다. 업로드 성공 후 서버 imageUrl을 따로 받아야 한다.

Q. 파일을 바꾸면 이전 preview는 어떻게 해?
A. 이전 preview URL을 revoke하고 새 파일의 preview URL을 만든다.

Q. 파일 업로드 중 버튼을 disabled 해야 해?
A. 중복 업로드를 막기 위해 업로드 중에는 버튼을 disabled 처리하는 것이 좋다.

Q. 업로드 실패 시 선택한 파일은 지워야 해?
A. 보통 유지하는 것이 좋다. 사용자가 다시 시도할 수 있어야 한다.

Q. validation error와 upload error는 달라?
A. 다르다. validation error는 요청 전 파일 검증 실패이고 upload error는 서버 요청 실패다.

Q. 업로드 진행률은 꼭 보여줘야 해?
A. 파일이 작으면 필수는 아니지만 대용량 파일이나 느린 네트워크에서는 유용하다.

Q. 파일과 글 내용을 한 번에 보낼 수 있어?
A. 가능하다. FormData에 JSON part와 file part를 함께 넣어 multipart 요청으로 보낼 수 있다.

Q. 파일을 먼저 업로드하고 URL만 저장하는 방식도 가능해?
A. 가능하다. 파일 업로드 API가 imageUrl이나 fileId를 반환하면 이후 JSON 요청에 포함할 수 있다.

Q. 어떤 방식이 더 좋아?
A. Backend API 설계와 트랜잭션 요구사항에 따라 다르다.

Q. 파일 업로드 성공 후 글 작성 실패하면 어떻게 해?
A. orphan file이 생길 수 있으므로 Backend 정리 정책이나 실패 보상 처리를 고려해야 한다.

Q. 여러 파일은 FormData에 어떻게 넣어?
A. 같은 key로 여러 번 append한다. 예: `formData.append("images", file)` 반복.

Q. 파일 개수 제한은 Frontend에서 해야 해?
A. UX를 위해 Frontend에서 먼저 하고, Backend에서도 반드시 검증해야 한다.

Q. 선택한 파일 하나만 제거할 수 있어?
A. 가능하다. File 배열 상태에서 해당 index를 제거하면 된다.

Q. 다중 파일 업로드에서 일부만 실패하면 어떻게 해?
A. Backend API 정책에 따라 전체 실패 또는 부분 성공으로 처리할 수 있으므로 응답 구조를 확인해야 한다.

Q. 업로드 성공 후 뭘 저장해야 해?
A. Backend 응답에 따라 imageUrl, imageId, originalFileName 등을 상태에 저장한다.

Q. previewUrl과 imageUrl은 달라?
A. 다르다. previewUrl은 브라우저 임시 URL이고 imageUrl은 서버에 저장된 파일 접근 URL이다.

Q. 후속 요청에는 imageUrl을 보내야 해 imageId를 보내야 해?
A. Backend API 명세에 따라 다르다. 서버가 fileId를 기대하면 imageId를 보내야 한다.

Q. 업로드 응답 구조는 어디서 확인해?
A. Network 탭의 Response Body와 Backend API 명세를 확인한다.

Q. 업로드 전 선택한 파일 삭제는 API가 필요해?
A. 아니다. 아직 서버에 업로드하지 않았다면 Frontend state에서만 제거하면 된다.

Q. 이미 업로드된 파일 삭제는 API가 필요해?
A. 필요하다. 서버 저장소에서 삭제하려면 Backend Delete API를 호출해야 한다.

Q. 파일 교체는 어떻게 해?
A. 새 파일 업로드 후 기존 파일 삭제 또는 Backend replace API를 사용할 수 있다.

Q. 삭제 실패 시 UI에서 파일을 지워도 돼?
A. 권장하지 않는다. 서버 삭제 실패 시 UI와 서버 상태가 불일치할 수 있다.

Q. File Upload는 보안상 위험해?
A. 위험할 수 있다. 악성 파일, 경로 조작, 용량 공격, 권한 문제를 Backend에서 반드시 검증해야 한다.

Q. Frontend 파일 검증만으로 충분해?
A. 아니다. Frontend 검증은 우회 가능하므로 Backend 검증이 최종 기준이다.

Q. 파일명은 그대로 저장해도 돼?
A. 권장하지 않는다. 서버에서 안전한 저장 파일명으로 재생성하는 것이 좋다.

Q. 업로드 파일 URL은 모두 공개해도 돼?
A. 파일 성격에 따라 다르다. 민감 파일은 인증과 권한 검사를 거쳐 접근해야 한다.

Q. 파일 업로드가 실패하면 뭘 먼저 봐?
A. Network 탭에서 Request Payload, Content-Type, Authorization Header, Response Body를 확인한다.

Q. Backend에서 파일이 null로 들어가?
A. FormData key와 Backend가 기대하는 multipart field name이 일치하는지 확인해야 한다.

Q. 415 Unsupported Media Type은 왜 나?
A. Content-Type이나 multipart 요청 형식이 Backend가 기대하는 형식과 다를 때 발생할 수 있다.

Q. 업로드 성공했는데 이미지가 안 보여?
A. 응답 imageUrl, 정적 파일 접근 경로, storage 권한, CORS, 이미지 URL 유효성을 확인한다.

Q. File Upload에서 가장 흔한 실수는?
A. FormData key와 Backend multipart field name을 맞추지 않거나 Content-Type boundary를 깨뜨리는 것이다.

Q. 파일을 JSON body로 보내면 안 돼?
A. 일반 파일 업로드는 JSON body가 아니라 multipart FormData로 보내는 것이 일반적이다.

Q. previewUrl을 DB에 저장해도 돼?
A. 안 된다. previewUrl은 브라우저 임시 URL이므로 서버에서 반환한 imageUrl이나 fileId를 저장해야 한다.

Q. 업로드 API가 401이면 뭘 봐?
A. authApi 사용 여부와 Authorization Header 포함 여부를 Network 탭에서 확인해야 한다.

Q. Part09 File Upload의 목적은 뭐야?
A. Frontend Agent가 FormData와 multipart/form-data를 사용해 파일 업로드 API를 안정적으로 구현하게 만드는 것이다.

Q. Part09 다음에는 어떤 문서가 이어지면 좋아?
A. API Troubleshooting, CORS / 401 / 403 / 404 Debugging, API Testing, Authentication Frontend Flow 순서로 이어지는 것이 좋다.
