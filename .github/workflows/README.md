# GitHub Actions CI/CD 配置说明

本项目配置了 GitHub Actions 作为 CI/CD 系统，实现自动化测试和代码质量检查。

## Workflow 文件

### 1. `ci.yml` - 主 CI 流程
- **触发时机**: 推送到 main 分支，或创建 PR
- **测试矩阵**: Python 3.8, 3.9, 3.10, 3.11
- **功能**:
  - 运行所有测试
  - 检查代码覆盖率（必须 ≥ 80%）
  - 运行 flake8 代码质量检查
  - 上传覆盖率到 Codecov

### 2. `pr-check.yml` - PR 门禁
- **触发时机**: 创建、更新、重新打开 PR
- **功能**:
  - 强制要求所有测试通过
  - 强制要求覆盖率 ≥ 80%
  - 自动在 PR 中添加评论（成功/失败状态）
  - 检查目标分支的保护规则

## 启用门禁功能（必须配置）

要让 CI 成为真正的"门禁"，必须在 GitHub 仓库设置中配置分支保护规则：

### 配置步骤：

1. **进入仓库设置**
   - GitHub 仓库 → Settings → Branches

2. **添加保护规则**
   - 点击 "Add rule"
   - Branch name pattern: `main` (或 `develop`)
   - 勾选以下选项：
     - ✅ Require a pull request before merging
       - ✅ Require approvals: 至少 1 个 reviewer
     - ✅ Require status checks to pass before merging
       - 选择: `Test and Coverage` 和 `PR Test Gate`
     - ✅ Require branches to be up to date before merging
     - ✅ Do not allow bypassing the above settings

3. **保存规则**

### 效果：
- ❌ 测试失败 → **无法合并** PR
- ❌ 覆盖率 < 80% → **无法合并** PR
- ❌ 代码检查失败 → **无法合并** PR
- ✅ 所有检查通过 → **可以合并**

## 状态检查

创建 PR 后，你会在以下地方看到 CI 状态：

1. **PR 页面底部** - 显示所有 checks 的状态
2. **Actions 标签页** - 详细的运行日志
3. **PR 评论** - 自动添加的成功/失败消息

## 本地测试

在提交代码前，可以本地运行 CI 命令：

```bash
# 运行所有测试
pytest tests/ -v

# 检查覆盖率
pytest tests/ --cov=pistol_magazine --cov-report=term

# 代码质量检查
flake8 pistol_magazine tests/
```

## 环境变量（可选）

在仓库 Settings → Secrets 中可以配置：

- `CODECOV_TOKEN` - 上传覆盖率到 Codecov 的 token
