# 技术设计 (Technical Design)

## 2. API Design
### POST /api/user/preferences
- **Description**: Update user theme preference (Ref: Story-1, FR-01).
- **Body**: `{ "theme": "dark" | "light" | "system" }`

## 3. Frontend Implementation
### ThemeProvider
- **Logic**: Use `next-themes` to handle system preference detection (Ref: FR-01).
- **Storage**: Persist to `localStorage` (Ref: AC 2.3).
